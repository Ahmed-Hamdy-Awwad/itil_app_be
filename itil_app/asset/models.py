from django.db import models
from ..supplier.models import Supplier
from django.contrib.auth.models import User


class Asset(models.Model):
	service_tag = models.CharField(max_length=30)
	purchase_date = models.DateTimeField(blank=True, null=True)
	ip_address = models.GenericIPAddressField(blank=True, null=True)
	manufacturing_date = models.DateTimeField(null=True, blank=True)
	creation_user = models.ForeignKey(User, on_delete=models.PROTECT)
	mac_address = models.CharField(max_length=17, blank=True, null=True)
	cost = models.DecimalField(default=0, decimal_places=2, max_digits=10)
	supplier = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.PROTECT)
	last_user = models.ForeignKey(User, related_name='asset_last_user', null=True, blank=True, on_delete=models.PROTECT)
	current_user = models.ForeignKey(User, related_name='asset_current_user', null=True, blank=True, on_delete=models.PROTECT)

	def __str__(self):
		return self.service_tag