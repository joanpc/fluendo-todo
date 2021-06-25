from django.db import models


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', related_name='todo', on_delete=models.CASCADE)
