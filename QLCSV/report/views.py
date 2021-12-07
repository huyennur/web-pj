from django.contrib import messages
from report.models import Report
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from authentication.models import Account
from report.admin import ReportResource


def report(request):
    if (request.method == 'POST'):
        Name = request.POST['Name']
        Title = request.POST['Title']
        Messages = request.POST['Messages']
        Report(Name=Name, Title=Title, Messages=Messages).save()
        messages.success(
            request, 'Báo cáo thành công! Cảm ơn bạn đã đóng góp ý kiến. Chúng tôi sẽ phản hồi nhanh nhất có thể!')
        return HttpResponseRedirect(request.path)
    else:
        user = Account.objects.get(Username=request.session['username'])
        reports = Report.objects.all()
        if (user.Group.name == 'staff'):
            return render(request, 'report_staff.html', {'reports': reports})
        else:
            return render(request, 'report.html')


def export_report(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        dataset = ReportResource().export()
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

    return render(request, 'export_report.html')
