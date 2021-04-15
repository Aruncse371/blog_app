from django.db import models
from django.conf import settings
user=settings.AUTH_USER_MODEL
gender=[("Male",1),("Female",2)]
# Create your models here.
class Details(models.Model):
    u_name = models.CharField(max_length=20)
    u_pwd = models.TextField(max_length=20)
    u_email = models.CharField(max_length=30)
    u_number = models.CharField(max_length=10)
    def __str__(self):
        return self.u_name


class Login(models.Model):
    u_name = models.CharField(max_length=20)
    u_pwd = models.CharField(max_length=20)
    def __str__(self):
        return self.u_name

class Data(models.Model):
    u_content = models.TextField(max_length=10000,null=False,blank=False)
    u_author = models.ForeignKey(user,on_delete=models.CASCADE,default=1)
    u_title = models.CharField(max_length=500,null=True,blank=True)
    u_image = models.ImageField(upload_to='images',default=None,blank=True,null=True)
    u_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.u_name

class Gender(models.Model):
    u_gender = models.CharField(max_length=6,choices= gender,default="Male")
# class Date(models.Model):
    # date = models.DateField(auto_now_add=)