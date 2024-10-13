from django.db import models
from django.contrib.auth.models import User


class Jobs(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    joined_date = models.DateField(null=False, auto_now=True, editable=False)

def __str__(self):
     return self.firstname