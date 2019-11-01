from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Course(models.Model):
    Course_Name=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.Course_Name

class Batch(models.Model):
    Select_Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Batch_Code=models.CharField(max_length=150,unique=True)
    Active_Status=models.IntegerField(default=1)
    Date=models.DateField()
    Fees=models.CharField(max_length=190)
    def __str__(self):
        return self.Batch_Code
class Trainer(models.Model):
    Name=models.CharField(max_length=250,unique=True)
    Phone_No = models.CharField(max_length=10)
    Email = models.EmailField()
    Verify_Email = models.EmailField()
    Password = models.CharField(max_length=150)
    def __str__(self):
        return self.Name
from timetable.models import ClassRoom
class User(models.Model):
    User_Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=150)
    def __str__(self):
        return self.User_Email

class Payment(models.Model):
    Type=models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.Type

class Register(models.Model):
    Name=models.CharField(max_length=150)
    Qualification=models.CharField(max_length=250)
    Address=models.TextField()
    Phone_No=models.CharField(max_length=10)
    Email=models.EmailField()
    Verify_Email=models.EmailField()
    Password=models.CharField(max_length=150)
    Select_Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Select_Batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    Payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
class HrUser(models.Model):
    Name = models.CharField(max_length=150)
    Phone_No = models.CharField(max_length=10)
    Email = models.EmailField()
    Verify_Email = models.EmailField()
    Password = models.CharField(max_length=150)

class ApprovedTable(models.Model):
    Select_Batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    Start_Time = models.TimeField()
    End_Time = models.TimeField()
    Class_Room=models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    Date=models.DateField()
    def __str__(self):
        return str(self.Date)