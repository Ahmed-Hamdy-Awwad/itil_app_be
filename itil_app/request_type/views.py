from .models import RequestType
from rest_framework import viewsets, permissions
from .serializers import GetRequestTypeSerializer


class RequestTypeView(viewsets.ModelViewSet):
	filter_fields = ('name',)
	# permission_classes = [permissions.DjangoModelPermissions]

	def get_queryset(self):
		return RequestType.objects.all()

	def get_serializer_class(self):
		return GetRequestTypeSerializer