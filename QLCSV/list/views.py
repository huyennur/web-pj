from django.shortcuts import render
from django.http import HttpResponse, response
from authentication.models import Student, Account, Job
from tablib import Dataset
from authentication.admin import StudentsResource
from authentication.admin import SalaryResource, JobResource, GPAResource
from django.shortcuts import render, redirect
from authentication.models import Account, School, Student, Account, GPA
from django.views.generic import View
import csv
import io
from authentication.models import Student, Account, School, Job, Address
from django.contrib.auth.models import Group
from tablib import Dataset
import json
from django.db.models import Q

addresses = ["An Giang", "Bà rịa – Vũng tàu", "Bắc Giang", "Bắc Kạn", "Bạc Liêu",
             "Bắc Ninh", "Bến Tre", "Bình Định", "Bình Dương", "Bình Phước", "Bình Thuận",
             "Cà Mau", "Cần Thơ", "Cao Bằng", "Đà Nẵng", "Đắk Lắk", "Đắk Nông", "Điện Biên",
             "Đồng Nai", "Đồng Tháp", "Gia Lai", "Hà Giang", "Hà Nam", "Hà Nội", "Hà Tĩnh",
             "Hải Dương", "Hải Phòng", "Hậu Giang", "Hòa Bình", "Hưng Yên", "Khánh Hòa",
             "Kiên Giang", "Kon Tum", "Lai Châu", "Lâm Đồng", "Lạng Sơn", "Lào Cai", "Long An",
             "Nam Định", "Nghệ An", "Ninh Bình", "Ninh Thuận", "Phú Thọ", "Phú Yên", "Quảng Bình", "Quảng Nam",
             "Quảng Ngãi", "Quảng Ninh", "Quảng Trị", "Sóc Trăng", "Sơn La", "Tây Ninh", "Thái Bình", "Thái Nguyên",
             "Thanh Hóa", "Thừa Thiên Huế", "Tiền Giang", "Thành phố Hồ Chí Minh", "Trà Vinh", "Tuyên Quang", "Vĩnh Long",
             "Vĩnh Phúc", "Yên Bái", "Nước ngoài"]

majors = ["CN1", "CN2", "CN3", "CN4", "CN5",
          "CN6", "CN7", "CN8", "CN9", "CN10", "CN11"]


def list(request):
    students = Student.objects.all()
    currentAddress = Address.objects.all()
    grades = School.objects.all().values('Grade').distinct()
    jobs = Job.objects.all()
    return render(
        request, "list.html", {'students': students, 'grades': grades, 'addresses': addresses,
                               'currentAddress': currentAddress, 'majors': majors, 'jobs': jobs}
    )


def listAdmin(request):
    return render(request, 'list-admin.html')


def exportList(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        print(StudentsResource())
        dataset = GPAResource().export()

        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
        elif file_format == 'XLSX':
            response = HttpResponse(
                dataset.xlsx, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'
            return response
        elif file_format == 'XLS':
            response = HttpResponse(
                dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse(
                dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response

    return render(request, 'export.html')


def importList(request):
    if request.method == 'POST':
        file_format = request.POST['file_format']
        employee_resource = GPAResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(
                new_employees.read().decode('utf-8'), format='csv')
            result = employee_resource.import_data(dataset, dry_run=True)
        elif file_format == 'JSON':
            imported_data = dataset.load(
                new_employees.read().decode('utf-8'), format='json')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True)
        elif file_format == 'XLS':
            imported_data = dataset.load(
                new_employees.read().decode('utf-8'), format='xls')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True)
        elif file_format == 'XLSX':
            imported_data = dataset.load(
                new_employees.read().decode('utf-8'), format='xlsx')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            # Import now
            employee_resource.import_data(dataset, dry_run=False)

    return render(request, 'import.html')


def delete(request):
    if request.method == 'POST':
        usernames = request.POST.getlist('Username[]')
        for id in usernames:
            student = Account.objects.get(Username=id)
            student.delete()
    return render(request, "list.html", {})


def search(request):
    grade = request.POST['grade']
    if grade == '---Chọn khối---':
        grade = ''
    address = request.POST['address']
    if address == '---Chọn nơi làm việc---':
        address = ''
    major = request.POST['major']
    if major == '---Chọn chuyên ngành---':
        major = ''
    if address == 'Nước ngoài':
        students = Student.objects.filter(school__Grade__icontains=grade).filter(MSSV__in=Job.objects.filter(
            Major__icontains=major).values_list('MSSV')).exclude(MSSV__in=Address.objects.filter(JobAddress__in=addresses).values_list('MSSV'))
    else:
        students = Student.objects.filter(school__Grade__icontains=grade).filter(MSSV__in=Job.objects.filter(Major__icontains=major).values_list(
            'MSSV')).filter(MSSV__in=Address.objects.filter(JobAddress__icontains=address).values_list('MSSV'))
    if grade == '' and address == '' and major == '':
        students = Student.objects.all()
    data = []
    for student in students:
        date = student.DateOfBirth
        formatedDate = date.strftime("%d-%m-%Y")
        address = ''
        major = ''
        for adr in Address.objects.all():
            if adr.MSSV == student.user.Username:
                address = adr.JobAddress
                break
        for mj in Job.objects.all():
            if mj.MSSV == student.user.Username:
                major = mj.Major
                break
        data.append({
            'Username': student.user.Username,
            'FirstName': student.user.FirstName,
            'LastName': student.user.LastName,
            'currentAddress': address,
            'Major': major,
            'DateOfBirth': json.dumps(formatedDate, default=str),
            'Gender': student.Gender,
            'PhoneNumber': student.PhoneNumber,
        })
    return HttpResponse(json.dumps({"data": data}), content_type='application/json')


def add(request):
    if request.method == "POST":
        MSSV = request.POST['MSSV']
        Password = request.POST['Password']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        DateOfBirth = request.POST['DateOfBirth']
        Email = request.POST['Email']
        Gender = request.POST['Gender']
        Address = request.POST['Address']
        StartTimeShool = request.POST['StartTimeShool']
        FinishTimeSchool = request.POST['FinishTimeSchool']
        Major = request.POST['Major']
        Grade = request.POST['Grade']
        Class = request.POST['Class']

        group = Group.objects.get(name="student")

        user = Account.objects.create(Username=MSSV, Password=Password,
                                      FirstName=FirstName, LastName=LastName, Email=Email, Group=group)

        Student(user=user, MSSV=MSSV,  DateOfBirth=DateOfBirth,
                Gender=Gender,  PhoneNumber=None, Address=Address, AmountOfDonation=None).save()

        School(Student=user.student, MSSV=MSSV, StartTimeShool=StartTimeShool, FinishTimeSchool=FinishTimeSchool,
               Grade=Grade, Class=Class, Achievement="Không").save()

        print(MSSV)
        Job(MSSV=MSSV, Major=Major).save()
        return render(request, 'add.html')
    else:
        return render(request, 'add.html')
