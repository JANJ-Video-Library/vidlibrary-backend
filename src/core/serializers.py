from rest_framework import serializers
from .models import Video, VideoType

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'title', 'link', 'category'
        )

class VideoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoType
        fields = (
            'type',
        )