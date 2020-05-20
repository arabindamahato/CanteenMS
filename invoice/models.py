from django.db import models
from user.models import User
# from menu.models import Canteen

# Create your models here.

class Invoice(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	invoice_number = models.CharField(default="", blank=True, max_length=50)
	date_of_issue = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="+")
	# canteen = models.ForeignKey(Canteen, on_delete=models.CASCADE, null=True, related_name="+")
	unit_price = models.DecimalField(max_digits=8, decimal_places=2, default="")
	discount_amount = models.DecimalField(max_digits=8, decimal_places=2, default="")
	total_price = models.DecimalField(max_digits=8, decimal_places=2, default="")
	is_active = models.BooleanField(default=True)
	
	# class Meta:
	# 	ordering = ['-created', ]

	def __str__(self):
		return "({})".format(
			 self.invoice_number
		)
		