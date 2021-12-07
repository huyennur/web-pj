from django.db import models
from django.contrib.auth.models import Group
from django.urls import reverse


class Account(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    Group = models.ForeignKey(
        Group, related_name='group', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Username)


class Students(models.Model):
    MSSV = models.CharField(max_length=150)
    Password = models.CharField(max_length=150)
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    PhoneNumber = models.CharField(max_length=150)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=1)
    Hometown = models.CharField(max_length=150)
    StartTimeShool = models.DateField()
    FinishTimeSchool = models.DateField()
    Achievement = models.CharField(max_length=500)
    AmountOfDonation = models.IntegerField()
    JobStatus = models.CharField(max_length=150)

    def __str__(self):
        return str(self.MSSV)


class Student(models.Model):
    user = models.OneToOneField(
        Account, null=True, blank=True, on_delete=models.CASCADE)
    MSSV = models.CharField(max_length=150)
    Gender = models.CharField(max_length=150)
    DateOfBirth = models.DateField()
    PhoneNumber = models.CharField(max_length=150, null=True, blank=True)
    Address = models.CharField(max_length=150)
    AmountOfDonation = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.MSSV)


class School(models.Model):
    Student = models.ForeignKey(
        Student, null=True, blank=True, on_delete=models.CASCADE)
    MSSV = models.CharField(max_length=150)
    StartTimeShool = models.DateField()
    FinishTimeSchool = models.DateField()
    Grade = models.CharField(max_length=150)
    Class = models.CharField(max_length=150)
    Achievement = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.MSSV)


class Job(models.Model):
    MSSV = models.CharField(max_length=150)
    Major = models.CharField(max_length=150)
    JobStatus = models.CharField(max_length=150)
    JobName = models.CharField(max_length=300)
    JobAddress = models.CharField(max_length=300)
    TimeToStart = models.DateField(null=True, blank=True)
    Feature = models.CharField(max_length=150)

    def __str__(self):
        return self.MSSV


class GPA(models.Model):
    MSSV = models.CharField(max_length=150)
    GPA = models.CharField(max_length=150)


class Salary(models.Model):
    MSSV = models.CharField(max_length=150)
    Salary = models.CharField(max_length=150)

    def __str__(self):
        return str(self.MSSV)


class Address(models.Model):
    MSSV = models.CharField(max_length=150)
    Address = models.CharField(max_length=150)
    CurrentAddress = models.CharField(max_length=150)
    JobAddressWorld = models.CharField(max_length=150)
    JobAddress = models.CharField(max_length=150)
