from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=50)
    salary = models.IntegerField()
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name
