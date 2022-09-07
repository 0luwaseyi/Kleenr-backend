from django.db import models

# Create your models here.

class signup(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    password  = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname


class login(models.Model):
    email = models.CharField(max_length=120)
    password  = models.CharField(max_length=50)