from rest_framework import serializers
from cartaeleanor.models import Index

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = '__all__'