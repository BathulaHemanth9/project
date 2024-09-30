from django.db import models

# Create your models here.

class student(models.Model):
    stid=models.IntegerField(primary_key=True)
    stname=models.CharField(max_length=20)
    userid=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mail=models.CharField(max_length=20)
    mobile_no=models.CharField(max_length=20)
    def __str__ (self):
        return self.stname

class teacher(models.Model):
    tid = models.IntegerField(primary_key=True)
    tname = models.CharField(max_length=20)
    salary = models.IntegerField()
    userid=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mobile_no=models.CharField(max_length=20)
    mail=models.CharField(max_length=20)
    def __str__ (self):
        return self.tname
    
class Admin(models.Model):
    adminid = models.IntegerField(primary_key=True)
    adminname = models.CharField(max_length=20)
    salary = models.IntegerField()
    userid=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mobile_no=models.CharField(max_length=20)
    mail=models.CharField(max_length=20)
    def __str__ (self):
        return self.adminname