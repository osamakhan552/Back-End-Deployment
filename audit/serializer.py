from rest_framework import serializers
from .models import *

class auditSerializer(serializers.ModelSerializer):
    class Meta:
        model = audit
        fields = '__all__'


class auditTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = auditType
        fields = '__all__'