from django.db import models
from Login.models import MyUser
from Databases.models import Department

class Degrees(models.Model):
    university = models.CharField(max_length=100)
    year_obtained = models.IntegerField(null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)
    major = models.CharField(max_length=40, null=True)

    TYPE_CHOICES = [
         ('Cử nhân', 'Cử nhân'),
         ('Thạc sĩ', 'Thạc sĩ'),
         ('Tiến sĩ', 'Tiến sĩ'),
     ]
    type = models.CharField(max_length=20, null=True, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.type} ngành {self.major}"
    
class Teacher(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    username = models.OneToOneField(MyUser, on_delete=models.CASCADE, null = True)
    phone_number = models.CharField(max_length=15, null=True)
    date_of_birth = models.DateField(null=True)
    hometown = models.CharField(max_length=40, null=True)
    avatar = models.ImageField(upload_to="Avatar/Teacher/", null=True, blank=True)

    GENDER_CHOICES = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
    ]
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
    
    