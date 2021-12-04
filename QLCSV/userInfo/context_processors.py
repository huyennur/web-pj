from authentication.models import Account, Student, School, Job
from django.shortcuts import render


def basePage(request):
    if 'username' in request.session:
        curr_user = Account.objects.get(Username=request.session['username'])
        if curr_user.Group.name == 'student':
            curr_user_job = Job.objects.get(MSSV=request.session['username'])
            return {"curr_user": curr_user, "curr_user_job": curr_user_job}
        return {"curr_user": curr_user}
    return ""
