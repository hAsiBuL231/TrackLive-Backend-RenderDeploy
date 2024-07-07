from rest_framework import serializers
from .models import SOSHistory

class HistoricalRecordField(serializers.ListField):
    child = serializers.DictField()

    def to_representation(self, data):
        return super().to_representation(data.values())

class SOSHistorySerializer(serializers.ModelSerializer):
    history = HistoricalRecordField(read_only=True)

    class Meta:
        model = SOSHistory
        fields = "__all__"
        # fields = ['id', 'name', 'email', 'number', 'location', 'latitude', 'longitude', 'phone_numbers']
