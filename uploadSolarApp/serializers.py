from rest_framework import serializers
from .models import Solar
class solarSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Solar
        fields = '__all__'

