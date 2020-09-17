from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=1000)
    category = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title