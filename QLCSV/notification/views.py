from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from authentication.models import Account
from notification.models import Notification

# Create your views here.


def all_notifi(request):
    curr_user = Account.objects.get(Username=request.session['username'])
    if (curr_user.Group.name == 'staff'):
        notice = Notification.objects.filter(user=curr_user).order_by('-date')
    else:
        notice = Notification.objects.filter(
            Q(user=curr_user) | Q(type='Admin')).order_by('-date')

    paginator = Paginator(notice, 20)

    pageNumber = request.GET.get('page')

    try:
        notice = paginator.page(pageNumber)
    except PageNotAnInteger:
        notice = paginator.page(1)
    except EmptyPage:
        notice = paginator.page(paginator.num_pages)

    return render(request, 'notification.html', {"Noticess": notice})
