# BÀI TẬP LỚN WEB: Trang web quản lý cựu sinh viên
Nhóm 6 lớp 2122I_INT3306_22 - UET

## Giới thiệu
Đây là bài tập lớn cuối kỳ của nhóm 6 về trang web quản lý hệ thống cựu sinh viên. Trang web này dành cho các sinh viên đã tốt nghiệp và đã ra trường, muốn liên hệ cũng như hỗ trợ nhà trường. Ngoài ra trang web này còn giúp nhà trường quản lý và liên hệ với cựu sinh viên để thông báo các sự kiện diễn ra của trường.

## Công nghệ sử dụng
- **Frontend:** HTML, CSS, JAVASCRIPT, BOOTSTRAP
- **Backend:** Django
- **Database:** Mysql PHPmyadmin

## Tạo database:
Sử dụng trang web PHPmyadmin: tạo database mới có tên **qlcsv** và không đặt mật khẩu (lưu ý cài đặt đúng với các yêu cầu: 'NAME': 'qlcsv', 'USER': 'root', 'password': "", 'HOST': '127.0.0.1', 'PORT': '3306')

## Cách chạy chương trình:

1. Cài đặt Django, mysqlclient, pillow, django-import-export
```
pip install django
pip install mysqlclient
pip install Pillow
pip install django-import-export
```

2. Chạy các lệnh để kết nối với database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

2. Chạy lệnh sau để tạo ra superuser để quản lý toàn bộ database ở django admin:
```
python3 manage.py createsuperuser
```

2. Trong database **qlcsv**, thêm vào bảng **auth_group** 2 object: 
* id = 1, name = staff  
* id = 2, name = student
trong đó staff là người quản trị của trang web và student là người dùng trang web.

3. Trong database **qlcsv**, thêm dữ liệu vào các bảng **authentication_account**, **authentication_student**, **authentication_school**, **authentication_job**, **authentication_address**, **authentication_salary** để có thể trải nghiệm được trang web.

4. Cuối cùng chạy lệnh 
```
python3 manage.py runserver
```

## Lưu ý:
Ở file /authentication/views.py:
```
def forgotPassEmail(request):
    if(request.method == 'POST'):
        Email = request.POST['Email']
        body = render_to_string('/Users/dongochuyen/Desktop/web-pj/QLCSV/authentication/templates/sendMail.txt')
        send_mail('Reset your password', body, Email, [Email])
        messages.success(request, "Thư đã được gửi vào mail của bạn. Xin hãy kiểm tra lại hộp thư và cài đặt lại mật khẩu.")
    return render(request, 'forgotPassEmail.html')
```
chú ý thay đổi đường dẫn của file **sendMail.txt** đúng với đường dẫn ở trong project.


