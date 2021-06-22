from .models import RequestType
from rest_framework import serializers


class GetRequestTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = RequestType
		fields = ('id', 'name')