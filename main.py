from setup import*
from django.db import models


class Role(models.Models):
    name = models.CharField(max_length=200)







class User(models.Model):
    name = models.CharField(max_legth=200)
    email = models.EmailField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


