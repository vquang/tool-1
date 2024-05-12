#!/bin/bash

# Kiểm tra số lượng tham số
if [ "$#" -ne 3 ]; then
    echo "Sử dụng: $0 <username> <ip_address> <password>"
    exit 1
fi

# Gán các tham số cho biến tương ứng
SSH_USER="$1"
SSH_IP="$2"
SSH_PASSWORD="$3"

# Tạo command string chứa lệnh mở terminal mới và kết nối SSH
COMMAND="gnome-terminal -- sshpass -p $SSH_PASSWORD ssh $SSH_USER@$SSH_IP"

# Thực thi command
eval $COMMAND
