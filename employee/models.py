from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    address = models.CharField(max_length=500, null=True)
    nic = models.CharField(max_length=15, unique=True)
    mobile = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    created_by = models.ForeignKey(Employee)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Department(models.Model):
    name = models.CharField()
