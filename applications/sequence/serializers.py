from rest_framework import serializers
from .models import Sequence

class FlattnesSequenceSerializer(serializers.Serializer):
    sequence = serializers.ListField()

class FlattnesSequenceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence
        fields = (
            'id',
            'value',
        )