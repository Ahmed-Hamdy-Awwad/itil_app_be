from django.contrib import admin
from .ticket.models import Ticket
from .request_type.models import RequestType

admin.site.register(Ticket)
admin.site.register(RequestType)
