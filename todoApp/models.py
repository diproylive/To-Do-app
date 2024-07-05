from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.text