from rest_framework import serializers
from apps.personas.models import Meta

class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meta
        fields = ['met_codigo']