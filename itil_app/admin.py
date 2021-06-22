from .asset.models import Asset
from django.contrib import admin
from .ticket.models import Ticket
from .supplier.models import Supplier
from .request_type.models import RequestType

admin.site.register(Asset)
admin.site.register(Ticket)
admin.site.register(Supplier)
admin.site.register(RequestType)
