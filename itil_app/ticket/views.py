from .models import Ticket
from .serializers import GetTicketSerializer
from rest_framework import viewsets, permissions


class TicketView(viewsets.ModelViewSet):
	filter_fields = ('id',)
	# permission_classes = [permissions.DjangoModelPermissions]

	def get_queryset(self):
		return Ticket.objects.all()

	def perform_create(self, serializer):
		serializer.save(reporter=self.request.user)

	def get_serializer_class(self):
		return GetTicketSerializer