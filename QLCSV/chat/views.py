from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from authentication.models import Account
from .models import PrivateRoom, Message
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import json

# Create your views here.
def index(request):
    user = Account.objects.get(Username=request.session['username'])
    # rooms = PrivateRoom.objects.filter(Q(user1=user) | Q(user2=user)).filter(lastMessage__isnull=False).distinct().order_by('-lastUpdateTime')
    rooms = PrivateRoom.objects.filter(Q(user1=user) | Q(user2=user)).distinct().order_by('-lastUpdateTime')
    return render(request, 'chat.html', {
        'rooms': rooms,
        'username': mark_safe(json.dumps(request.session['username'])),
        'image': mark_safe(json.dumps(user.profile.image.url)),
    })

def loadContacts(request):
    if request.method == 'POST':
        user = Account.objects.get(Username=request.session['username'])
        rooms = PrivateRoom.objects.filter(Q(user1=user) | Q(user2=user)).distinct().order_by('-lastUpdateTime')
        data = []
        for room in rooms:
            data.append({
                'id': room.id,
                'user1': user_to_json(room.user1),
                'user2': user_to_json(room.user2),
                'lastMessage': room.lastMessage
                })
    return HttpResponse(json.dumps({"data": data}), content_type='application/json')

def user_to_json(user):
    return {
        'username': user.Username,
        'name': user.FirstName + " " + user.LastName,
        'image': user.profile.image.url
    }   
    
def getMessages(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        if room_id is not None:
            messages =  Message.objects.filter(room__id=room_id).order_by('timestamp')
            data = []
            for message in messages:
                data.append({
                    'user': message.user.Username,
                    'content': message.content,
                    'image': message.user.profile.image.url,
                    })
            return HttpResponse(json.dumps({"data": data}), content_type='application/json')
    return HttpResponse("No data!")

def createMsg(request):
    if request.method == 'POST':
        username = request.POST['username']
        room_id = request.POST['room_id']
        message = request.POST['message']
        
        user = Account.objects.get(Username=username)
        Message.objects.create(user=user, room_id=room_id, content=message)
        room = PrivateRoom.objects.get(pk=room_id)
        room.lastMessage = message
        room.save()
        return HttpResponse('Created a new message!')
    return HttpResponse('Fail to create a new message!')
    
def checkRoom(request):
    if request.method == 'POST':
        receiver = request.POST['toUser']
        acc1 = Account.objects.get(Username=request.session['username'])
        acc2 = Account.objects.get(Username=receiver)
        lookup = (Q(user1=acc1) & Q(user2=acc2)) | (Q(user1=acc2) & Q(user2=acc1))
        if PrivateRoom.objects.filter(lookup).exists():
            index(request)
        else:
            newroom = PrivateRoom.objects.create(user1=acc1, user2=acc2)
            user = Account.objects.get(Username=request.session['username'])
            rooms = PrivateRoom.objects.filter(Q(user1=user) | Q(user2=user)).filter(lastMessage__isnull=False).exclude(id=newroom.id).distinct().order_by('-lastUpdateTime')
            return render(request, 'chat.html', {
                'rooms': rooms,
                'username': mark_safe(json.dumps(request.session['username'])),
                'image': mark_safe(json.dumps(user.profile.image.url)),
            })
    return HttpResponse('Suceces!')

def room(request, toUser):
    user = Account.objects.get(Username=request.session['username'])
    rooms = PrivateRoom.objects.filter(Q(user1=user) | Q(user2=user)).distinct()
    return render(request, 'chat.html', {
        'rooms': rooms,
        'username': mark_safe(json.dumps(request.session['username'])),
    })
    