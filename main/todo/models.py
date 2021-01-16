from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null= False)
    text = models.CharField(max_length=2000, null= True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.name