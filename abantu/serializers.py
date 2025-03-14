from rest_framework import serializers
from .models import Abantu

class AbantuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abantu
        fields = '__all__'