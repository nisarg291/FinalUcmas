from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date
# # Create your models here.


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
    date=models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.StudentFirstName+" "+self.StudentMiddleName+" "+self.StudentLastName+" Profile"

