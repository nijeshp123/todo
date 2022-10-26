from email.policy import default
from enum import auto
from django.db import models

# Create your models here.


class Todos(models.Model):
    task_name=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_name