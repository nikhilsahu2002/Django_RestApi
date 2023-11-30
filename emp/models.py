from django.db import models

# Create your models here.
class Company(models.Model):
    Company_id = models.AutoField(primary_key=True) 
    name = models.CharField( max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField( max_length=50)
    added_date = models.DateTimeField(auto_now=True)
    Activate = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name= models.CharField( max_length=50)
    email =models.CharField( max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(('manager','manager'),('Software Developer','Software Developer'),('project Leader','project')))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)