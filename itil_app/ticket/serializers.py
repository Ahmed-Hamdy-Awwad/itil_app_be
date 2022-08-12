from .models import Ticket
from rest_framework import serializers
from ..users.serializers import GetUserSerializer


class GetTicketSerializer(serializers.ModelSerializer):
	reporter = GetUserSerializer()
	class Meta:
		model = Ticket
		fields = ('id', 'description', 'reporter', 'status')

class CreateTicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = ('description',)