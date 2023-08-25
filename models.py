from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
