from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from datetime import datetime as dt

class CustomUserManager(BaseUserManager):
    def create_user(self, password, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        return self.create_user(password, **extra_fields)



class Student(AbstractUser):

    #objects = CustomUserManager()

    username = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,blank=True)
    date = models.DateField(default = dt.now)
    batch = models.IntegerField(blank=True,default=2020)
    instution = models.CharField(max_length=100,blank=True)
    subject = models.CharField(max_length=100,blank=True)
    bio = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='images/',blank=True)


class Post(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Reference to the Student model
    text = models.TextField()
    modified_date = models.DateTimeField(auto_now=True)