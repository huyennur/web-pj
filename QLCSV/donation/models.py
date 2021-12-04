from django.db import models
from authentication.models import Student


class Donation(models.Model):
    StudentCode = models.ForeignKey(Student, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Email = models.CharField(max_length=150, null=True)
    PhoneNumber = models.CharField(max_length=150, null=True)
    BankAccountNumber = models.CharField(max_length=20)
    AmountOfDonation = models.IntegerField()
    DonationDate = models.DateField()
    Messages = models.CharField(max_length=500, null=True)


class Regis_teach(models.Model):
    StudentCode = models.ForeignKey(Student, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=150, null=True)
    LastName = models.CharField(max_length=150, null=True)
    teach_title = models.CharField(max_length=150)
    teach_date = models.DateField()
    teach_mess = models.CharField(max_length=500, null=True)


class Introduce(models.Model):
    StudentCode = models.ForeignKey(Student, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=150, null=True)
    LastName = models.CharField(max_length=150, null=True)
    intro_title = models.CharField(max_length=150)
    intro_content = models.CharField(max_length=2000, default='')
