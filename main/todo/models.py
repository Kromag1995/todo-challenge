from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null= False)
    text = models.CharField(max_length=2000, null= True)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=now())
    def __str__(self):
        return self.title