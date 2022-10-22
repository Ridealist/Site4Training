from rest_framework import serializers
from ..models import Training

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = (
            'title',
            'website',
            'type',
            'description',
            'time',
            'price',
            'url',
            'image',
        )