from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50, null=True, default="")
    credit = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = name = models.CharField(max_length=50, null=True, default="")

    def __str__(self):
        return self.name
    
class Major(models.Model):
    name = name = models.CharField(max_length=50, null=True, default="")

    def __str__(self):
        return self.name