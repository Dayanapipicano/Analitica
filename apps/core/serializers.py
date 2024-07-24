from rest_framework import serializers
from apps.personas.models import Meta,Estrategia

class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meta
        fields = ['met_id','met_codigo']
        
class EstrateiaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estrategia
        fields = [
            'est_nombre'
        ]