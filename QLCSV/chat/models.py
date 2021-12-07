from django.db import models
from authentication.models import Student, School, Account

# Create your models here.


class PrivateRoom(models.Model):
    user1 = models.ForeignKey(
        Account, null=True, on_delete=models.SET_NULL, related_name='user1')
    user2 = models.ForeignKey(
        Account, null=True, on_delete=models.SET_NULL, related_name='user2')
    lastUpdateTime = models.DateTimeField(null=True, blank=True, auto_now=True)
    lastMessage = models.TextField(default="", max_length=100)

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ['user1', 'user2']


class Message(models.Model):
    user = models.ForeignKey(
        Account, related_name='user_msg', on_delete=models.CASCADE)
    room = models.ForeignKey(PrivateRoom, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.Username

    def last_15_messages():
        return Message.objects.order_by('-timestamp').all()[:15]


class MessageNotification(models.Model):
    receiver = models.ForeignKey(
        Account, related_name='notification_receiver', on_delete=models.CASCADE)
    sender = models.ForeignKey(
        Account, related_name='notification_sender', on_delete=models.CASCADE)
    room = models.ForeignKey(PrivateRoom, null=True, on_delete=models.CASCADE)
    isUnseen = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.room.id)
