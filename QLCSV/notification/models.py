from django.db import models
from django.db.models.fields import DateField
from forum.models import Post, Comment
from authentication.models import Account
from datetime import datetime
from connection.models import Group_post
from connection.models import Group_comment

# Create your models here.


class Notification (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    g_post = models.ForeignKey(Group_post, on_delete=models.CASCADE, null=True)
    cmt = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    g_cmt = models.ForeignKey(
        Group_comment, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=100, default='Admin')
    date = models.DateTimeField(default=datetime.now, blank=True)
