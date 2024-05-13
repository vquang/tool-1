
# HƯỚNG DẪN CÀI ĐẶT THƯ VIỆN VÀ CHẠY TOOL 1

## Mô tả công cụ
Là một công cụ giúp kiểm thử web-server, sử dụng các phương thức tấn công phổ biến như: tấn công từ điển, sql-injection, quét cổng dịch vụ...; tích hợp các công cụ mạnh mẽ như sqlmap, hydra, nmap...

## Cài đặt các công cụ tích hợp

Cài đặt công cụ: nmap, hydra, sqlmap, sshpass, curl:

```bash
  sudo apt install nmap hydra sqlmap sshpass curl
```

Cài đặt framework nodejs (nếu câu lệnh **npm install 20** báo không tìm thấy npm thì restart lại máy rồi chạy lại câu lệnh đó):

```bash
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
  nvm install 20
  node -v
  npm -v
```
## Cài đặt các thư viện cho python

Cài đặt thư viện flask và beautifulsoup4:

```bash
  pip install Flask beautifulsoup4 
```

## Chạy tool

Tại thư mục tool-1, chạy file sau:

```bash
  ./run.sh
```
