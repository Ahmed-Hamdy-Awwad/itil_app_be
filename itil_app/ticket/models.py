from django.db import models
from django.contrib.auth.models import User
from ..request_type.models import RequestType


class Ticket(models.Model):
	STATUS_CHOICES=[
		('Pending', 'Pending'),
		('Opened', 'Opened'),
		('Closed', 'Closed')
	]
	description = models.TextField()
	creation_date = models.DateTimeField(auto_now_add=True)
	closing_date = models.DateTimeField(null=True, blank=True)
	response_date = models.DateTimeField(null=True, blank=True)
	request_type = models.ForeignKey(RequestType, on_delete=models.PROTECT)
	status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='Pending')
	reporter = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ticket_reporter')
	assignee = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, related_name='ticket_assignee')

	def __str__(self):
		return self.description