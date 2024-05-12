#!/bin/bash

# Thông tin đăng nhập
username="user"
ip="192.168.100.164"
password="12345678"


# Tạo command để thực hiện telnet cùng với username và password
telnet_command="telnet $ip <<EOF
sleep 1
echo $username
sleep 1
echo $password
sleep 1
EOF"

# Mở terminal mới và thực hiện telnet cùng với username và password
gnome-terminal -- bash -c "$telnet_command;

