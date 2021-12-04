from django.shortcuts import render
from django.http import HttpResponse, response
from authentication.models import Student, Account
from tablib import Dataset
from authentication.admin import StudentsResource
from authentication.admin import SalaryResource, JobResource, GPAResource


def list(request):
    return render(request, 'list.html')


def listAdmin(request):
    return render(request, 'list-admin.html')


def exportList(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        account = JobResource()
        dataset = account.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response
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
    # if request.method == 'POST':
    #     file_format = request.POST['file-format']
    #     employee_resource = EmployeeResource()
    #     dataset = Dataset()
    #     new_employees = request.FILES['importData']

    #     if file_format == 'CSV':
    #         imported_data = dataset.load(
    #             new_employees.read().decode('utf-8'), format='csv')
    #         result = employee_resource.import_data(dataset, dry_run=True)
    #     elif file_format == 'JSON':
    #         imported_data = dataset.load(
    #             new_employees.read().decode('utf-8'), format='json')
    #         # Testing data import
    #         result = employee_resource.import_data(dataset, dry_run=True)
    #     elif file_format == 'XLS':
    #         imported_data = dataset.load(
    #             new_employees.read().decode('utf-8'), format='xls')
    #         # Testing data import
    #         result = employee_resource.import_data(dataset, dry_run=True)
    #     elif file_format == 'XLSX':
    #         imported_data = dataset.load(
    #             new_employees.read().decode('utf-8'), format='xlsx')
    #         # Testing data import
    #         result = employee_resource.import_data(dataset, dry_run=True)

    #     if not result.has_errors():
    #         # Import now
    #         employee_resource.import_data(dataset, dry_run=False)

    return render(request, 'import.html')
