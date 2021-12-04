from django.db import models
from authentication.models import Student
from datetime import datetime
# Create your models here.


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    #leader = models.ForeignKey(Student, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=150)
    group_infor = models.CharField(max_length=1000)
    group_area = models.CharField(max_length=20)
    group_class = models.CharField(max_length=20)
    group_member = models.IntegerField(default=0)

# class Member(models.Model):
#    id = models.AutoField(primary_key=True)
#    groupID = models.ForeignKey(Group, on_delete=models.CASCADE)
#    member = models.ForeignKey(Student, on_delete=models.CASCADE)


class Group_post(models.Model):
    id = models.AutoField(primary_key=True)
    groupID = models.ForeignKey(Group, on_delete=models.CASCADE)
    g_post_user = models.ForeignKey(Student, on_delete=models.CASCADE)
    g_post_title = models.CharField(max_length=150)
    g_post_content = models.CharField(max_length=2000)
    g_post_date = models.DateTimeField(default=datetime.now, blank=True)
    g_post_comment = models.IntegerField(default=0)
    g_post_image = models.ImageField(upload_to="group_images", default='')


class Group_comment(models.Model):
    id = models.AutoField(primary_key=True)
    g_postID = models.ForeignKey(Group_post, on_delete=models.CASCADE)
    g_cmt_user = models.ForeignKey(Student, on_delete=models.CASCADE)
    g_cmt_content = models.CharField(max_length=300)
    g_cmt_date = models.DateTimeField(default=datetime.now, blank=True)
    g_cmt_image = models.ImageField(upload_to="group_images", default='')
