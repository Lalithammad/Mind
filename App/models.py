from django.db import models

# Create your models here.
class Employee(models.Model):
    email          = models.EmailField(unique=True)
    firstname      = models.CharField(null=True,blank=True,max_length=50)
    lastname       = models.CharField(null=True,blank=True,max_length=50)
    password       = models.CharField(null=True,blank=True,max_length=40)
    address        = models.CharField(null=True,blank=True,max_length=200)
    dob            = models.DateField()
    company        = models.CharField(null=True,blank=True,max_length=100)
    mobile         = models.IntegerField(null=True,blank=True)
    city           = models.CharField(null=True,blank=True,max_length=50)

    
    def __str__(self):
        return self.email