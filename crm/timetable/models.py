from django.db import models
from datetime import datetime,timedelta
from app1.models import Batch,Trainer

# Create your models here.

class ClassRoom(models.Model):
    Class_Name = models.CharField(max_length=256,unique=True)
    No_of_Students=models.IntegerField()
    def __str__(self):
        return self.Class_Name
def next_day():
    return datetime.now() + timedelta(days=1)
class TimeTable(models.Model):
    Select_Batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    Start_Time = models.TimeField(default=datetime.now)
    End_Time = models.TimeField()
    Class_Room=models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    Date=models.DateField(default=next_day)
class ToApproveTB(models.Model):
    Select_Batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    Start_Time = models.TimeField()
    End_Time = models.TimeField()
    Class_Room=models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    Date=models.DateField()
