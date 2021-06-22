from .models import Asset
from .serializers import GetAssetSerializer
from rest_framework import viewsets, permissions


class AssetView(viewsets.ModelViewSet):
	filter_fields = ('id',)
	# permission_classes = [permissions.DjangoModelPermissions]

	def get_queryset(self):
		return Asset.objects.all()

	def perform_create(self, serializer):
		serializer.save(creation_user=self.request.user)

	def get_serializer_class(self):
		return GetAssetSerializer