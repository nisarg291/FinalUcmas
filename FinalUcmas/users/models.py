from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date
import datetime
# # Create your models here.

class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.SmallIntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # stu_id = models.AutoField(primary_key=True)
    StudentUserName=models.CharField(max_length=50,default="")
    StudentFirstName=models.CharField(max_length=50,default="")
    StudentMiddleName=models.CharField(max_length=50,default="")
    StudentLastName=models.CharField(max_length=50,default="")
    # StudentImage = models.ImageField(default="default.jpg",upload_to='student/images')
    BirthDate = models.CharField(max_length=50,default="")
    Gender=models.CharField(max_length=10,default="")
    StudentEmail=models.EmailField(max_length=254,default="")
    std=models.IntegerField(default=0)
    Enroll=models.IntegerField(default=0)
    ucmaslevel=models.IntegerField(default=1)
    SchoolName=models.CharField(max_length=100,default="")
    Hobbies=models.CharField(max_length=200,default="")
    Refference=models.CharField(max_length=100,default="")
    Ressidence=models.TextField(default="")
    JoiningDate=models.DateTimeField(default=datetime.datetime.now(),null=True)
    def __str__(self):
        return self.StudentFirstName+" "+self.StudentMiddleName+" "+self.StudentLastName+" Profile"
    
    def __save__(self,*args,**kwargs):
        print("enter here");
        self.JoiningDate = datetime.datetime.now()
        super(Profile, self).save(*args, **kwargs)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    seen = models.BooleanField(default=False)
 
