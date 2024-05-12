

FORMS = []
PORTS = []
ACCOUNT_WEB = []
ACCOUNT_SSH = []
DBS = []
BACK_DB = ''
TASK_ID = ''
IP = ''
TABLES = []
COLUMNS = []

USERLIST = 'userlist.txt'
PASSLIST = 'passlist.txt'
ACCOUNT_WEB_LIST = 'accweblist.txt'
ACCOUNT_SSH_LIST = 'accsshlist.txt'
PORTS_LIST = 'ports.xml'

# COLUMNS
def setColumns(value):
    global COLUMNS
    COLUMNS = value

def getColumns():
    return COLUMNS

# TABLES
def setTables(value):
    global TABLES
    TABLES = value

def getTables():
    return TABLES

# IP
def setIP(value):
    global IP
    IP = value

def getIP():
    return IP

# TASK_ID SQL
def setTaskID(value):
    global TASK_ID
    TASK_ID = value

def getTaskID():
    return TASK_ID

# BACK_DB
def setBackDB(value):
    global BACK_DB
    BACK_DB = value

def getBackDB():
    return BACK_DB

# DBS
def setDBS(value):
    global DBS
    DBS = value

def getDBS():
    return DBS

# FORMS
def setFORMS(value):
    global FORMS
    FORMS = value

def getFORMS():
    return FORMS

# PORTS
def setPORTS(value):
    global PORTS
    PORTS = value

def getPORTS():
    return PORTS

# ACCOUNT_WEB
def setACCOUNT_WEB(value):
    global ACCOUNT_WEB
    ACCOUNT_WEB = value

def getACCOUNT_WEB():
    return ACCOUNT_WEB

# ACOUNT_SSH
def setACCOUNT_SSH(value):
    global ACCOUNT_SSH
    ACCOUNT_SSH = value

def getACCOUNT_SSH():
    return ACCOUNT_SSH

def reset():
    global FORMS
    global PORTS
    global ACCOUNT_WEB
    global ACCOUNT_SSH
    global DBS
    global BACK_DB
    global IP
    global TABLES
    global COLUMNS

    FORMS = []
    PORTS = []
    ACCOUNT_WEB = []
    ACCOUNT_SSH = []
    DBS = []
    BACK_DB = ''
    IP = []
    TABLES = []
    COLUMNS = []

    with open(ACCOUNT_WEB_LIST, "w") as file:
        file.write("")
    with open(ACCOUNT_SSH_LIST, "w") as file:
        file.write("")  
    with open(PORTS_LIST, "w") as file:
        file.write("")