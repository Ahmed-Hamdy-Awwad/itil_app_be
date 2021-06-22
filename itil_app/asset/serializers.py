from .models import Asset
from rest_framework import serializers
from ..users.serializers import GetUserSerializer
from ..supplier.serializers import GetSupplierSerializer


class GetAssetSerializer(serializers.ModelSerializer):
	last_user = GetUserSerializer()
	current_user = GetUserSerializer()
	supplier = GetSupplierSerializer()
	
	class Meta:
		model = Asset
		fields = ('service_tag', 'purchase_date', 'ip_address', 'manufacturing_date', 'mac_address', 'cost', 'supplier', 'last_user', 'current_user')