from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import Student, School, Job, GPA, Account, Address

addresses = ["An Giang", "Bà rịa – Vũng tàu", "Bắc Giang", "Bắc Kạn", "Bạc Liêu",
             "Bắc Ninh", "Bến Tre", "Bình Định", "Bình Dương", "Bình Phước", "Bình Thuận",
             "Cà Mau", "Cần Thơ", "Cao Bằng", "Đà Nẵng", "Đắk Lắk", "Đắk Nông", "Điện Biên",
             "Đồng Nai", "Đồng Tháp", "Gia Lai", "Hà Giang", "Hà Nam", "Hà Nội", "Hà Tĩnh",
             "Hải Dương", "Hải Phòng", "Hậu Giang", "Hòa Bình", "Hưng Yên", "Khánh Hòa",
             "Kiên Giang", "Kon Tum", "Lai Châu", "Lâm Đồng", "Lạng Sơn", "Lào Cai", "Long An",
             "Nam Định", "Nghệ An", "Ninh Bình", "Ninh Thuận", "Phú Thọ", "Phú Yên", "Quảng Bình", "Quảng Nam",
             "Quảng Ngãi", "Quảng Ninh", "Quảng Trị", "Sóc Trăng", "Sơn La", "Tây Ninh", "Thái Bình", "Thái Nguyên",
             "Thanh Hóa", "Thừa Thiên Huế", "Tiền Giang", "Thành phố Hồ Chí Minh", "Trà Vinh", "Tuyên Quang", "Vĩnh Long",
             "Vĩnh Phúc", "Yên Bái"]


def editProfile(request):
    user = Account.objects.get(Username=request.session['username'])
    if request.method == 'POST':

        # Update value in 'Student' table
        user.FirstName = request.POST.get('FirstName')
        user.LastName = request.POST.get('LastName')
        user.Email = request.POST.get('Email')

        # Update user avatar
        # Check if user updated image
        if request.FILES.get('avatar', False):
            user.profile.image = request.FILES['avatar']

        # If user is a student
        if user.Group.name == 'student':
            editStudent = Student.objects.get(MSSV=request.session['username'])
            editSchool = School.objects.get(MSSV=request.session['username'])
            editJob = Job.objects.get(MSSV=request.session['username'])
            editAddress = Address.objects.get(MSSV=request.session['username'])
            editStudent.DateOfBirth = request.POST.get('DateOfBirth')
            editStudent.PhoneNumber = request.POST.get('PhoneNumber')
            editStudent.Gender = request.POST.get('Gender')
            editStudent.Address = request.POST.get('Address')
            editAddress.JobAddress = request.POST.get('JobAddress')
            editJob.Feature = request.POST.get('Feature')
            if editAddress.JobAddress in addresses:
                editAddress.JobAddressWorld = "Trong nước"
            else:
                editAddress.JobAddressWorld = "Ngoài nước"

            # Update value in 'School' table
            # editSchool.Achievement = request.POST.get('Achievement')

            # Update value in 'Job' table
            editJob.JobStatus = request.POST.get('JobStatus')
            editJob.JobName = request.POST.get('JobName')
            editJob.JobAddress = request.POST.get('JobAddress')
            editJob.TimeToStart = request.POST.get('TimeToStart')

            editAddress.save()
            editStudent.save()
            editSchool.save()
            editJob.save()
        user.profile.save()
        user.save()
        return redirect(f'/userInfo/profile/{user.Username}')
    return render(request, 'userInfoEdit.html')


def profile(request, user_mssv):
    user = Account.objects.get(Username=user_mssv)
    if user.Group.name == 'student':
        userSchool = School.objects.get(MSSV=user_mssv)
        userJob = Job.objects.get(MSSV=user_mssv)
        return render(request, 'userInfo.html', {"user": user, "userSchool": userSchool, "userJob": userJob})
    return render(request, 'userInfo.html', {"user": user})
