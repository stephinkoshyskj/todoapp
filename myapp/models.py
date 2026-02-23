from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):

    title = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now=True)

    status = models.BooleanField(default=False)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):

        self.title



