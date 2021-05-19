from django.db import models
from PIL import Image
# Create your models here.
class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    StudentUserName=models.CharField(max_length=50,default="")
    StudentFirstName=models.CharField(max_length=50)
    StudentMiddleName=models.CharField(max_length=50)
    StudentLastName=models.CharField(max_length=50)
    # StudentImage = models.FileField(default="default.jpg",upload_to='student/images')
    BirthDate = models.CharField(max_length=50,default="")
    Gender=models.CharField(max_length=10)
    StudentEmail=models.EmailField(max_length=254,default="")
    std=models.IntegerField()
    Enroll=models.IntegerField()
    ucmaslevel=models.IntegerField(default=1)
    SchoolName=models.CharField(max_length=100)
    Hobbies=models.CharField(max_length=200)
    Refference=models.CharField(max_length=100)
    Ressidence=models.TextField()
    FatherName = models.CharField(max_length=70)
    FatherQualification=models.CharField(max_length=200)
    FatherOccupation=models.CharField(max_length=100)
    FatherEmail=models.EmailField(max_length=254,default="")
    FatherContact1=models.CharField(max_length=10)
    FatherContact2=models.CharField(max_length=10)
    MotherName = models.CharField(max_length=70)
    MotherQualification=models.CharField(max_length=100)
    MotherOccupation=models.CharField(max_length=100)
    MotherEmail=models.EmailField(max_length=254,default="")
    MotherContact1=models.CharField(max_length=10)
    MotherContact2=models.CharField(max_length=10)
    date=models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.StudentFirstName+" "+self.StudentMiddleName+" "+self.StudentLastName
