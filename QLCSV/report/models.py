from django.db import models
from django.db.models.fields import DateTimeField
from datetime import datetime


class Report(models.Model):
    Name = models.CharField(max_length=50)
    Title = models.CharField(max_length=100)
    Messages = models.CharField(max_length=1000)
    ReportDate = models.DateTimeField(default=datetime.now, blank=True)
