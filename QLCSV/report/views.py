from django.contrib import messages
from report.models import Report
from django.shortcuts import render
from django.http.response import HttpResponseRedirect


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
        return render(request, 'report.html')
