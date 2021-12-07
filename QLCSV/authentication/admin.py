from django.db import models
from django.contrib import admin
from authentication.models import Student, Account, School, Job, GPA, Address, Salary, Students
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from import_export import resources

admin.site.site_header = "QLCSV ADMIN PAGE"
admin.site.site_url = "/authentications/index"
admin.site.index_title = "Welcome to QLCSV admin site"


class AccountManagement(admin.ModelAdmin):
    fields = ['Username', 'Password', 'FirstName',
              'LastName', 'Email', 'Group_id']


class StudentManagement(admin.ModelAdmin):
    fields = ['MSSV', 'DateOfBirth', 'Gender',
              'PhoneNumber', 'Address', 'AmountOfDonation']


class StudentsManagement(admin.ModelAdmin):
    fields = ['MSSV', 'DateOfBirth', 'Gender',
              'PhoneNumber', 'Address', 'AmountOfDonation']


class SchoolManagement(admin.ModelAdmin):
    fields = ['MSSV', 'StartTimeShool', 'FinishTimeSchool',
              'Grade', 'Class', 'Achievement']


class JobManagement(admin.ModelAdmin):
    fields = ['MSSV', 'Major', 'JobStatus',
              'JobName', 'JobAddress', 'TimeToStart']


class GPAManagement(admin.ModelAdmin):
    fields = ['MSSV', 'GPA']


class SalaryManagement(admin.ModelAdmin):
    fields = ['MSSV', 'Major', 'JobStatus',
              'JobName', 'JobAddress', 'TimeToStart']


class AddressManagement(admin.ModelAdmin):
    fields = ['MSSV', 'Major', 'JobStatus',
              'JobName', 'JobAddress', 'TimeToStart']


# # admin.site.register(Students, StudentManagement)


class AccountResource(resources.ModelResource):
    class Meta:
        model = Account


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


class StudentsResource(resources.ModelResource):
    class Meta:
        model = Students
        fields = ('MSSV', 'Password', )


class SchoolResource(resources.ModelResource):
    class Meta:
        model = School


class JobResource(resources.ModelResource):
    class Meta:
        model = Job
        field = ('id', 'MSSV', 'JobName', )


class GPAResource(resources.ModelResource):
    class Meta:
        model = GPA


class AddressResource(resources.ModelResource):
    class Meta:
        model = Address


class SalaryResource(resources.ModelResource):
    class Meta:
        model = Salary
        fields = ('MSSV', 'Salary', )


class StudentAdmin(ImportExportModelAdmin):
    list_display = ('MSSV', 'DateOfBirth', 'Gender',
                    'PhoneNumber', 'Address', 'AmountOfDonation')
    resources_class = StudentResource


class AccountAdmin(ImportExportModelAdmin):
    list_display = ('Username', 'Password', 'FirstName',
                    'LastName', 'Email', 'Group_id')
    resources_class = AccountResource


class SchoolAdmin(ImportExportModelAdmin):
    list_display = ('MSSV', 'StartTimeShool', 'FinishTimeSchool',
                    'Grade', 'Class', 'Achievement')
    resources_class = SchoolResource


class JobAdmin(ImportExportModelAdmin):
    list_display = ('MSSV', 'Major', 'JobStatus',
                    'JobName', 'JobAddress', 'TimeToStart')
    resources_class = JobResource


class GPAAdmin(ImportExportModelAdmin):
    list_display = ('MSSV', 'GPA')
    resources_class = GPAResource


class SalaryAdmin(ImportExportModelAdmin):
    list_display = ('MSSV', 'Salary')
    resources_class = SalaryResource


class AddressAdmin(ImportExportModelAdmin):
    list_display = ('MSSV', 'Address', 'CurrentAddress',
                    'JobAddressWorld', 'JobAddress')
    resources_class = AddressResource


admin.site.register(Account, AccountAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(GPA, GPAAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Salary, SalaryAdmin)
