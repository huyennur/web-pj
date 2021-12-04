from django.db import models
from django.db.models.fields import DateTimeField
from datetime import datetime
from authentication.models import Student
from userInfo.models import Profile


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    post_user = models.ForeignKey(Student, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=150)
    post_content = models.CharField(max_length=2000)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    post_like = models.IntegerField(default=0)
    post_comment = models.IntegerField(default=0)
    post_image = models.ImageField(upload_to="post_images", default='')


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    cmt_user = models.ForeignKey(Student, on_delete=models.CASCADE)
    cmt_content = models.CharField(max_length=300)
    cmt_like = models.IntegerField(default=0)
    cmt_date = models.DateTimeField(default=datetime.now, blank=True)
    cmt_image = models.ImageField(upload_to="post_images", default='')
