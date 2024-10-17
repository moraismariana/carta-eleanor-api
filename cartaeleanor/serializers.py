from rest_framework import serializers
from cartaeleanor.models import Index, IndexText, IndexImage, IndexBackground, IndexPseudoImage

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = '__all__'

class IndexTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexText
        fields = '__all__'

class IndexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexImage
        fields = '__all__'

class IndexBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexBackground
        fields = '__all__'
    
class IndexPseudoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexPseudoImage
        fields = '__all__'