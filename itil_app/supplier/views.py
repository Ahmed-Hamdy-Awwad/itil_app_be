from .models import Supplier
from .serializers import GetSupplierSerializer
from rest_framework import viewsets, permissions


class SupplierView(viewsets.ModelViewSet):
	filter_fields = ('id',)
	# permission_classes = [permissions.DjangoModelPermissions]

	def get_queryset(self):
		return Supplier.objects.all()

	def get_serializer_class(self):
		return GetSupplierSerializer