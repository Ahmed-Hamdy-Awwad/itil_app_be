from .models import Supplier
from rest_framework import serializers


class GetSupplierSerializer(serializers.ModelSerializer):

	class Meta:
		model = Supplier
		fields = ('id', 'name', 'phone', 'address')