# **Thông tin dịch vụ**
		
| Địa chỉ IP      | Các port đang mở |
| ----------- | ----------- |
| 192.168.19.116  | TCP: 42, 53, 80, 135, 445, 3389, 5985, 49667, 49670, 49671   |
|    | UDP: 53,137  |

# **Khởi tạo shell với quyền user thường**

---

**Lỗ hổng đã khai thác**: Khai thác tài nguyên chia sẻ trên dịch vụ SMB (port 445) bằng tài khoản guest.

**Giải thích về lỗ hổng**: Dịch vụ smb được thiết lập cho chúng ta có thể truy cập được cái tài nguyên được chia sẻ bằng tài khoản guest. Hacker có thể lợi dụng tài khoản này để tiến hành khai thác các thông tin được chia sẻ.

**Khuyến nghị vá lỗ hổng:** Disable tài khoản guest hoặc không lưu trữ các thông tin quan trọng khi có sử dụng tài khoản guest để chia sẻ thông tin trên dịch vụ SMB.

**Mức độ ảnh hưởng:** Khai thác được thông tin chứng thực của user sammy

**Cách thức khai thác:** 

Đầu tiên, chúng ta sẽ thực hiện công việc quen thuộc là sử dụng một đoạn script để phát hiện nhanh các port đang mở. Sau đó, chúng ta tiếp tục thực hiện nmap với các option `-A` (dùng để phát hiện dịch vụ đang chạy trên port, version các dịch vụ, thực hiện các default script scan, traceroute và phát hiện hệ điều hành đang chạy của máy nạn nhân) và `-Pn` (để bỏ quan việc xác định host còn sống hay không).

Chúng ta có thể thấy rằng chúng ta có khá nhiều dịch vụ có thể khai thác được như là `http(80)`, `MSRPC(135)`, `smb(445)`, `remote desktop(3389)`, `winrm(5985)`. Thông thường chúng ta sẽ bắt đầu với http nhưng do có sự xuất hiện của tài khoản guest ở dịch vụ smb như đã thấy ở kết quả scan trên (phần smb-security-mode cho bạn nào tìm hoài không thấy) nên ta sẽ bắt đầu với smb.
Thực hiện kiểm tra các tài nguyên được chia sẻ và quyền truy cập các tài nguyên đó bằng `smbmap`.
 
Ta có thể thấy được rằng folder Backups là folder duy nhất ta có quyền truy cập với user guest nên ta sẽ thực hiện mount folder Backups hoặc sử dụng smbclient để kết nối hoặc trực tiếp download folder về máy để phân tích.
 
Từ hình trên ta có thể thấy được rằng ta có duy nhất một folder tên là `WindowsImageBackup`. Tiếp tục đi sâu vào folder thì ta thấy được rất nhiều file và folder khác.
 
Tuy nhiên nếu đi tiếp vào folder `Backup 2020-11-30 102804` thì ta tìm thấy được một số `vhdx image` .
 
Các image này có thể là back up cho Sammy-PC và có thể có nhiều thông tin quý giá nên chúng ta sẽ bắt đầu từ image này.
Vì image `88e506b5-0000-0000-0000-602200000000.vhdx` có kích thước rất lớn và sẽ mất rất lâu để tải về máy nên chúng ta sẽ thực hiện mount image này để tiết kiệm thời gian. 
Sử dụng guestmount; với option `–add` để chọn image cần add, `--inspector` để mount file system như cách chúng được mount trong máy ảo, `--ro` để chế độ mount ở readonly; để mount image `88e506b5-0000-0000-0000-602200000000.vhdx` vào `/mnt/vhdx`.
 
Từ đây, chúng tôi đã tiến hành tìm kiếm trong thư mục users, program file, … nhưng không thu được kết quả. Tuy nhiên, vì đây là một image nên chúng ta có thể truy cập vào cả những file hệ thống mà bình thường chúng ta sẽ không thể truy cập. Ý tôi muốn nói ở đây là nơi lưu giữ hash password cho user.
Chúng ta tiến hành kiểm tra thư mục `Windows/System32/config` và thu được `SAM` và file `SYSTEM` (cho những ai không biết SAM và SYSTEM).
 
Tiến hành copy `SAM` và `SYSTEM` đến workspace và sử dụng `samdump2` (thằng này ra kết quả sai) hoặc `impacket-secretsdump` để tìm hash password của các user được lưu trong image này.
 
Dùng `crackstation.net` để crack hash password của user sammy.
 
Sử dụng thông tin chứng thực vừa tìm được của user sammy để đăng nhập vào máy nạn nhân thông qua dịch vụ winrm (có thử trên remote desktop nhưng thất bại).
 
**Hình ảnh minh chứng:**
 
 
**Nội dung tập tin `local.txt`:**
 
> FLAG: **flag{th4n_d1eu_da1_b1p}**

# **Privilege Escalation**


**Lỗ hổng đã khai thác:** PowerShell Transcript được lưu trữ dưới dạng plaintext
Giải thích lỗ hổng: A PowerShell transcript là một tệp văn bản đơn giản chứa lịch sử của tất cả các lệnh và đầu ra của chúng. Nếu attacker có quyền đọc các transcript đó thì họ có thể khai thác được thông tin được lưu lại trong transcript.

**Khuyến nghị vá lỗ hổng:** Không lưu trữ các transcript, phân quyền truy cập các transcript, mã hóa các transcript.
Mức độ ảnh hưởng: Khai thác được thông tin xác thực của user john (user thuộc administrator group)

**Cách thức khai thác:** 

Từ tài khoản user sammy mà ta sở hữu thì ta còn thấy được một user khác ngoài administrator
 
Kiểm tra thêm thì ta thấy user john sẽ thuộc vào group administrator nên chúng ta sẽ thực hiện khai thác các thông tin có liên quan đến user và một trong những cách khá hiệu quả là tìm kiếm tất cả các file có từ john.
 
Chúng ta sẽ thực hiện lệnh `ls` để liệt kê tất cả các file, `-R` để thực hiện liệt kê một cách đệ quy, `-Hidden` để tìm kiếm trên các file ẩn, `-EA SilentlyContinue` để loại bỏ các lỗi như không không có quyền truy cập đường dẫn và sau đó sử dụng `select-string` để tìm kiếm trong các file này các từ trùng khớp với từ `john`.
 
Chúng ta dùng lệnh `cat` để đọc file `Transcripts\20201130\PowerShell_transcript.VULNSRV04.LUdhZtw7.20201130225005.txt`
 
Sau một lúc đọc và phần tích file thì ta phát hiện ra quá trình user john được add password. (cho ai chưa biết cách add password bằng lệnh net)
 
Ta thấy được rằng mật khẩu không được gán trực tiếp cho user john mà được lưu trữ trong biến `$fo0`. Ngoài ra, ta còn thấy được rằng biến `$foo` sau khi được gán một đoạn mã base64 thì là được biến đổi và lưu vào trong biến `$fo0`.=> ta chỉ cần mô phỏng lại quá trình tạo ra biến `$fo0` như trên thì có thể lấy được mật khẩu của john.
 
Thực hiện đăng nhập vào máy nạn nhân bằng tài khoản của user john thông qua dịch vụ Remote Desktop bằng `xfreerdp` (không đăng nhập được trên winrm).
 
 
**Hình ảnh minh chứng:**
 
 
**Nội dung tập tin Proof.txt:** 
 
> **FLAG:** *flag{n0_dun9_th1_m1nh_ph4i_ch4m_n0_c4m_th1_m1nh_ph4i_xu6_n0_mu0n_su7_th1_m1nh_ch0_d0_lu0n}*





