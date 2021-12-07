from django.http.response import HttpResponseRedirect
from django.http import HttpResponse, response
from django.shortcuts import render
from donation.models import Donation, Introduce, Regis_teach
from authentication.models import Student, Account
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
import json


def donation(request):
    if (request.method == 'POST'):
        StudentCode = request.POST['StudentCode']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        Email = request.POST['Email']
        PhoneNumber = request.POST['PhoneNumber']
        BankAccountNumber = request.POST['BankAccountNumber']
        AmountOfDonation = request.POST['AmountOfDonation']
        DonationDate = request.POST['DonationDate']
        Messages = request.POST['Messages']

        try:
            donateUser = Student.objects.get(MSSV=StudentCode)
            donateUser.AmountOfDonation = F(
                'AmountOfDonation') + AmountOfDonation
            donateUser.save()
            Donation(StudentCode=donateUser, FirstName=FirstName, LastName=LastName, Email=Email,
                     PhoneNumber=PhoneNumber, BankAccountNumber=BankAccountNumber, AmountOfDonation=AmountOfDonation,
                     DonationDate=DonationDate, Messages=Messages).save()
            messages.success(request, 'Thông tin đã được ghi lại!')
        except Student.DoesNotExist as e:
            messages.success(request, 'Mã sinh viên không đúng')
        return HttpResponseRedirect(request.path, messages)
    else:
        user = Account.objects.get(Username=request.session['username'])
        donations = Donation.objects.all()
        students = Student.objects.all()
        if (user.Group.name == 'staff'):
            return render(request, 'donation_staff.html', {'donations': donations, 'students': students})
        else:
            return render(request, 'donation.html')


def registration_teaching(request):
    if (request.method == 'POST'):
        StudentCode = request.POST['StudentCode']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        teach_title = request.POST['teach_title']
        teach_date = request.POST['teach_date']
        teach_mess = request.POST['teach_mess']

        try:
            teach_user = Student.objects.get(MSSV=StudentCode)
            Regis_teach(StudentCode=teach_user, FirstName=FirstName, LastName=LastName,
                        teach_mess=teach_mess, teach_date=teach_date, teach_title=teach_title).save()
            messages.success(request, 'Thông tin đã được ghi lại!')
        except Student.DoesNotExist as e:
            messages.success(request, 'Mã sinh viên không đúng')
        return HttpResponseRedirect(request.path, messages)
    else:
        user = Account.objects.get(Username=request.session['username'])
        regis_teach = Regis_teach.objects.all()
        if (user.Group.name == 'staff'):
            return render(request, 'teaching-register-staff.html', {'regis_teach': regis_teach})
        else:
            return render(request, 'teaching-register.html')


def introduce(request):
    if (request.method == 'POST'):
        StudentCode = request.POST['StudentCode']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        intro_title = request.POST['intro_title']
        intro_content = request.POST['intro_content']

        try:
            intro_user = Student.objects.get(MSSV=StudentCode)
            Introduce(StudentCode=intro_user, FirstName=FirstName, LastName=LastName,
                      intro_title=intro_title, intro_content=intro_content).save()
            messages.success(request, 'Thông tin đã được ghi lại!')
        except Student.DoesNotExist as e:
            messages.success(request, 'Mã sinh viên không đúng')
        return HttpResponseRedirect(request.path, messages)
    else:
        user = Account.objects.get(Username=request.session['username'])
        introduces = Introduce.objects.all()
        if (user.Group.name == 'staff'):
            return render(request, 'introduce_staff.html', {'introduces': introduces})
        else:
            return render(request, 'introduce.html')

def searchDonation(request):
    if request.method == "POST":

        searchInput = request.POST["searchInputDonation"]
        students = Donation.objects.filter(StudentCode__MSSV__icontains=searchInput) or Donation.objects.filter(FirstName__icontains=searchInput)\
            or Donation.objects.filter(LastName__icontains=searchInput) or Donation.objects.filter(Messages__icontains=searchInput)
        data = []
        for student in students:
            date = student.DonationDate
            formatedDate = date.strftime("%d-%m-%Y")
            data.append({
                'StudentCode': student.StudentCode.MSSV,
                'FirstName': student.FirstName,
                'LastName' : student.LastName,
                'AmountOfDonation': student.AmountOfDonation,
                'Messages': student.Messages,
                'DonationDate' : json.dumps(formatedDate, default=str),
                })
        return HttpResponse(json.dumps({"data": data}), content_type='application/json')
    else:
        return render(request, "donation_staff.html", {})

def searchIntroduce(request):
    if request.method == "POST":

        searchInput = request.POST["searchInputIntroduce"]
        students = Introduce.objects.filter(StudentCode__MSSV__icontains=searchInput) or Introduce.objects.filter(FirstName__icontains=searchInput)\
            or Introduce.objects.filter(LastName__icontains=searchInput) or Introduce.objects.filter(intro_title__icontains=searchInput)\
                or Introduce.objects.filter(intro_content__icontains=searchInput)
        data = []
        for student in students:
            data.append({
                'StudentCode': student.StudentCode.MSSV,
                'FirstName': student.FirstName,
                'LastName' : student.LastName,
                'intro_title': student.intro_title,
                'intro_content': student.intro_content,
                })
        return HttpResponse(json.dumps({"data": data}), content_type='application/json')
    else:
        return render(request, "donation_staff.html", {})

def searchRegs(request):
    if request.method == "POST":

        searchInput = request.POST["searchInputRegs"]
        students = Regis_teach.objects.filter(StudentCode__MSSV__icontains=searchInput) or Regis_teach.objects.filter(FirstName__icontains=searchInput)\
            or Regis_teach.objects.filter(LastName__icontains=searchInput) or Regis_teach.objects.filter(teach_title__icontains=searchInput)\
                or Regis_teach.objects.filter(teach_mess__icontains=searchInput)
        data = []
        for student in students:
            date = student.teach_date
            formatedDate = date.strftime("%d-%m-%Y")
            data.append({
                'StudentCode': student.StudentCode.MSSV,
                'FirstName': student.FirstName,
                'LastName' : student.LastName,
                'teach_title': student.teach_title,
                'teach_mess': student.teach_mess,
                'teach_date' : json.dumps(formatedDate, default=str),
                })
        return HttpResponse(json.dumps({"data": data}), content_type='application/json')
    else:
        return render(request, "teaching-register-staff.html", {})
