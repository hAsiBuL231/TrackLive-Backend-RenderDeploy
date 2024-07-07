from rest_framework import serializers
from locations.models import LocationModel


class HistoricalRecordField(serializers.ListField):
    child = serializers.DictField()

    def to_representation(self, data):
        return super().to_representation(data.values())


class LocationSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="locations:locationmodel-detail")
    # history = serializers.ListField(child=serializers.DictField(), read_only=True)
    history = HistoricalRecordField(read_only=True)

    class Meta:
        model = LocationModel
        # fields = ('url', 'securityCode', 'taker', 'message', 'latitude', 'longitude') 
        fields = "__all__"


        