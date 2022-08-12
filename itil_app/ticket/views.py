from .models import Ticket
from rest_framework import viewsets, permissions
from .serializers import GetTicketSerializer, CreateTicketSerializer


class TicketView(viewsets.ModelViewSet):
	filter_fields = ('id',)
	# permission_classes = [permissions.DjangoModelPermissions]

	def get_queryset(self):
		return Ticket.objects.all()

	def perform_create(self, serializer):
		serializer.save(reporter_id=self.request.user.id)

	def get_serializer_class(self):
		serializer_type = self.request.query_params.get('serializer')
		if serializer_type == 'get':
			return GetTicketSerializer
		return CreateTicketSerializer