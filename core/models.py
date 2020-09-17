from django.db import models

# from django.contrib.auth import get_user_model

# User = get_user_model()
CATEGORIES = (
    ('Executive Speaker Series', 'Executive Speaker Series'),
    ('College 101', 'College 101'),
    ('Fireside Chat', 'Fireside Chat'),
    ('Other', 'Other')
)


# Create your models here.
class VideoType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class Video(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=1000)
    category = models.ForeignKey(VideoType, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

