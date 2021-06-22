from .models import Ticket
from rest_framework import serializers
from ..users.serializers import GetUserSerializer
from ..request_type.serializers import GetRequestTypeSerializer


class GetTicketSerializer(serializers.ModelSerializer):
	reporter = GetUserSerializer()
	assignee = GetUserSerializer()
	request_type = GetRequestTypeSerializer()
	class Meta:
		model = Ticket
		fields = ('id', 'description', 'reporter', 'request_type', 'closing_date', 'response_date', 'creation_date', 'assignee', 'status')