from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from donation.models import Donation, Introduce, Regis_teach
from authentication.models import Student
from django.contrib import messages
from django.db.models import F


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
        return render(request, 'introduce.html')
