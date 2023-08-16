from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.
class Course(models.Model):
    CourseName=models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.CourseName
class Slot(models.Model):
    Time_Slot=models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.Time_Slot    
class Batch(models.Model):
    Batch_Name=models.CharField(max_length=50)
    Time_Slot=models.ForeignKey(Slot,on_delete=models.CASCADE) 
    status=models.CharField(max_length=50)   
    
    def __str__(self):
        return self.Batch_Name

class Trainer(models.Model):
    FullName=models.CharField(max_length=50)
    Qualification=models.CharField(max_length=50)
    CourseName=models.ForeignKey(Course,on_delete=models.CASCADE) 
    

    def __str__(self):
        return self.FullName
class Student(models.Model):
    FullName=models.CharField(max_length=50)
    Qualification=models.CharField(max_length=50)
    CourseName=models.ForeignKey(Course,on_delete=models.CASCADE)
    trainer=ChainedForeignKey(Trainer,
        chained_field="CourseName",
        chained_model_field="CourseName",
        show_all=False,
        auto_choose=True,
        sort=True)
    Batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    Time=models.ForeignKey(Slot,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.FullName


