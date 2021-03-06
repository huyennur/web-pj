from django.core.checks import messages
from django.shortcuts import redirect, render, HttpResponse
from authentication.models import Student, Account, Students
from authentication.admin import JobResource
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from authentication.models import Job, School, GPA
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forum.models import Post
from django.db import connection
import json


def login(request):
    if request.method == "POST":
        try:
            Userdetails = Account.objects.get(
                Username=request.POST['MSSV'], Password=request.POST['Password'])
            # print("MSSV=", Userdetails)
            request.session['username'] = Userdetails.Username
            return redirect(f'/authentication/afterLogin/')
        except Account.DoesNotExist as e:
            messages.success(request, 'MSSV hoặc mật khẩu không tồn tại!')
    return render(request, 'login.html')


def logout(request):
    return render(request, 'login.html')


def UserReg(request):
    if(request.method == 'POST'):
        MSSV = request.POST['MSSV']
        Password = request.POST['Password']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        DateOfBirth = request.POST['DateOfBirth']
        Gender = request.POST['Gender']
        Email = request.POST['Email']
        PhoneNumber = request.POST['PhoneNumber']
        Address = request.POST['Address']
        AmountOfDonation = request.POST['AmountOfDonation']
        group = Group.objects.get(name="user")

        Student(MSSV=MSSV, Password=Password, FirstName=FirstName, LastName=LastName, DateOfBirth=DateOfBirth,
                Gender=Gender, Email=Email, PhoneNumber=PhoneNumber, Address=Address, AmountOfDonation=AmountOfDonation, Group=group).save()

        messages.success(request, 'The new user ' +
                         request.POST['MSSV'] + ' is added succesfully')
        return render(request, 'registration.html')
    else:
        return render(request, 'registration.html')


def studentSchoolReg(request):
    if(request.method == 'POST'):
        MSSV = request.POST['MSSV']
        StartTimeShool = request.POST['StartTimeShool']
        FinishTimeSchool = request.POST['FinishTimeSchool']
        Grade = request.POST['Grade']
        Class = request.POST['Class']
        Achievement = request.POST['Achievement']

        School(MSSV=MSSV, StartTimeShool=StartTimeShool, FinishTimeSchool=FinishTimeSchool,
               Grade=Grade, Class=Class, Achievement=Achievement).save()

        messages.success(request, 'The new user ' +
                         request.POST['MSSV'] + ' is added school info succesfully')
        return render(request, 'regSchool.html')
    else:
        return render(request, 'regSchool.html')


def studentJobReg(request):
    if(request.method == 'POST'):
        MSSV = request.POST['MSSV']
        Major = request.POST['Major']
        JobStatus = request.POST['JobStatus']
        JobName = request.POST['JobName']
        JobAddress = request.POST['JobAddress']
        TimeToStart = request.POST['TimeToStart']

        Job(MSSV=MSSV, Major=Major, JobStatus=JobStatus, JobName=JobName,
            JobAddress=JobAddress, TimeToStart=TimeToStart).save()

        messages.success(request, 'The new user ' +
                         request.POST['MSSV'] + ' is added job status info succesfully')
        return render(request, 'regJob.html')
    else:
        return render(request, 'regJob.html')


def studentGPAReg(request):
    if(request.method == 'POST'):
        MSSV = request.POST['MSSV']
        gpa = request.POST['GPA']

        GPA(MSSV=MSSV, GPA=gpa).save()
        messages.success(request, 'The new user ' +
                         request.POST['MSSV'] + ' is added gpa succesfully')
        return render(request, 'regGPA.html')
    else:
        return render(request, 'regGPA.html')


def forgotPassEmail(request):
    if(request.method == 'POST'):
        Email = request.POST['Email']
        body = render_to_string(
            '/Users/dongochuyen/Desktop/web-pj/QLCSV/authentication/templates/sendMail.txt')
        send_mail('Reset your password', body, Email, [Email])
        messages.success(
            request, "Thư đã được gửi vào mail của bạn. Xin hãy kiểm tra lại hộp thư và cài đặt lại mật khẩu.")
    return render(request, 'forgotPassEmail.html')


def forgotPass(request):
    if(request.method == 'POST'):
        try:
            mssv = Account.objects.get(Username=request.POST['MSSV'])
            newPass = request.POST['NewPass']
            renewPass = request.POST['RenewPass']
            E = Account.objects.get(Username=mssv)

            if(newPass == renewPass):
                E.Password = newPass
                E.save()
                messages.success(request, 'Thay đổi mật khẩu thành công!')
            else:
                messages.success(
                    request, 'Xin hãy nhập lại đúng mật khẩu mới !')
            return render(request, 'forgotPass.html')
        except Account.DoesNotExist as e:
            messages.success(request, 'MSSV không tồn tại!')
    return render(request, 'forgotPass.html')


def changePass(request):
    if(request.method == 'POST'):
        try:
            mssv = Account.objects.get(Username=request.POST['MSSV'])
            currentPass = request.POST['currentPass']
            newPass = request.POST['newPass']
            renewPass = request.POST['renewPass']
            E = Account.objects.get(Username=mssv)

            if(E.Password == currentPass and newPass == renewPass):
                E.Password = newPass
                E.save()
                messages.success(request, 'Thay đổi mật khẩu thành công!')
            else:
                messages.success(
                    request, 'Xin hãy nhập lại đúng mật khẩu!')
            return render(request, 'changePass.html')
        except Account.DoesNotExist as e:
            messages.success(request, 'MSSV không tồn tại!')
    return render(request, 'changePass.html')


# def afterLogin(request):
    # trong db của Khue, group của admin = 1 sau khi set group staff ở admin django
    # event = Post.objects.filter(post_user__Group=1).order_by('-post_date')[:2]
    # forum = Post.objects.exclude(post_user__Group=1).order_by('-post_date')[:2]
    # return render(request, 'afterLogin.html', {"Posts": event, "Forums": forum})
    # return render(request, 'afterLogin.html')


def event_forum(request):
    event = Post.objects.filter(post_user__Group=1).order_by('-post_date')

    paginator = Paginator(event, 10)

    pageNumber = request.GET.get('page')

    try:
        event = paginator.page(pageNumber)
    except PageNotAnInteger:
        event = paginator.page(1)
    except EmptyPage:
        event = paginator.page(paginator.num_pages)

    return render(request, 'forum.html', {"Posts": event})


def index(request):
    return render(request, 'index.html')


def search(request):
    if request.method == "POST":

        searchInput = request.POST.get("searchInput")
        students = Student.objects.filter(
            MSSV__contains=searchInput) or Student.objects.filter(FirstName__contains=searchInput) or School.objects.filter(Grade__contains=searchInput)
        return render(
            request, "search.html", {
                "searchInput": searchInput, 'students': students}
        )
    else:
        return render(request, "search.html", {})


temp = []
text = ""


def search(request):
    global temp
    global text
    if request.method == "POST":
        text = request.POST.get("searchInput")

        temp = Student.objects.filter(
            user__Username__icontains=text) or Student.objects.filter(user__FirstName__icontains=text)\
            or Student.objects.filter(school__Grade__icontains=text)

    students = temp
    searchInput = text
    paginator = Paginator(students, 10)

    pageNumber = request.GET.get('page')

    try:
        students = paginator.page(pageNumber)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(
        request, "search.html", {
            "searchInput": searchInput, 'students': students}
    )


def afterLogin(request):
    students = Student.objects.exclude(school__Achievement="Không")
    schools = School.objects.exclude(Achievement="Không")
    event = Post.objects.filter(post_user__Group=1).order_by('-post_date')[:4]
    forum = Post.objects.exclude(post_user__Group=1).order_by('-post_date')[:4]
    return render(request, 'afterLogin.html', {'students': students, 'schools': schools, "Posts": event, "Forums": forum})
