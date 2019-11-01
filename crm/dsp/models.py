from django.db import models
from datetime import datetime
from app1.models import Batch,Course,Trainer
# Create your models here.
class Status(models.Model):
    Status_Name=models.CharField(unique=True,max_length=200)
    def __str__(self):
        return self.Status_Name
class FeedbackOP(models.Model):
    options=models.CharField(unique=True,max_length=120)
    def __str__(self):
        return self.options
class SessionReport(models.Model):
    Student_Name=models.CharField(max_length=256)
    Trainer_Name=models.ForeignKey(Trainer,models.CASCADE)
    Topic=models.CharField(max_length=256)
    Status=models.ForeignKey(Status,on_delete=models.CASCADE)
    FeedBack=models.ForeignKey(FeedbackOP,on_delete=models.CASCADE)
    Date=models.DateField(default=datetime.now)
    def __str__(self):
        return str(self.Date)
