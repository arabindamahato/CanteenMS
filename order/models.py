from django.db import models

# Create your models here.


class OrderItem(models.Model):
	item_name = models.ForeignKey(Menu, on_delete=models.CASCADE, help_text="Breakfast, Lunch, etc")
	price = models.DecimalField(decimal_places=2, max_digits=10, default=0)

	def __str__(self):
		return f'{self.item_name.item}'


class Order(models.Model):title = models.CharField(blank=True, null=True, max_length=50)

	item = models.ForeignKey(OrderItem, null=True, on_delete=models.CASCADE)
	price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['-timestamp', ]


