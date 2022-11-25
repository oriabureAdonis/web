from rest_framework import serializers
from .models import drink

class drinkSerializer(serializers.ModelSerializer):
    class Meta:
         model = drink
         fields = ['id', 'name', 'description']