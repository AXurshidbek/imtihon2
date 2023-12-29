from rest_framework.serializers import ModelSerializer, Serializer
from .models import *
from django.core.exceptions import ValidationError

class SuvModelSerializer(ModelSerializer):
    class Meta:
        model=Suv
        fields='__all__'

class MijozModelSerializer(ModelSerializer):
    class Meta:
        model=Mijoz
        fields='__all__'




class BuyurtmaModelSerializer(ModelSerializer):
    class Meta:
        model=Buyurtma
        fields='__all__'
    def validate_qarz(self, qiymat):
        if qiymat > 4:
            raise ValidationError("Qarzingiz juda ko’p, buyurtma qilolmaysiz!")
        return qiymat

class AdminModelSerializer(ModelSerializer):

    class Meta:
        model=Admin
        fields='__all__'

class HaydovchiModelSerializer(ModelSerializer):
    class Meta:
        model=Haydovchi
        fields='__all__'
