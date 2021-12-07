from authentication.models import Account, Student, School, Job
from django.shortcuts import render
from notification.models import Notification
from chat.models import MessageNotification
from django.db.models import Q


def basePage(request):
    if 'username' in request.session:
        curr_user = Account.objects.get(Username=request.session['username'])
        notifs = MessageNotification.objects.filter(receiver=curr_user)
        if (curr_user.Group.name == 'staff'):
            notice = Notification.objects.filter(
                user=curr_user).order_by('-date')[:5]
        else:
            notice = Notification.objects.filter(
                Q(user=curr_user) | Q(type='Admin')).order_by('-date')[:5]
        print(notice)

        if curr_user.Group.name == 'student':
            curr_user_job = Job.objects.get(MSSV=request.session['username'])
            curr_user_school = School.objects.get(
                MSSV=request.session['username'])
            return {"curr_user": curr_user, "curr_user_school": curr_user_school, "curr_user_job": curr_user_job, "Notices": notice, 'notifs': notifs}
        return {"curr_user": curr_user, "Notices": notice, 'notifs': notifs}
    return ""
