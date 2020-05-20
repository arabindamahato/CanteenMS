from django.db import models
from user.models import User


# Create your models here.

class Menu(models.Model):
	name = models.CharField(default="Today's Menu", blank=True, null=True, max_length=255)
	description = models.TextField(blank=True, null=True)
	is_active = models.BooleanField(default=True)	
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, 
									on_delete=models.CASCADE, null=True,
									related_name='+')
	updated_by = models.ForeignKey(User, 
									on_delete=models.CASCADE, null=True,
									related_name='+')
	

	# class Meta:
	# 	ordering = ['-created', ]

	def __str__(self):
		return self.name




# class Canteen(models.Model):
# 	name = models.CharField(default="Desi Canteen", blank=True, null=True, max_length=255)
# 	address = models.TextField(blank=True, null=True)
# 	phone_no = models.CharField(blank=True, null=True, max_length=13)
# 	email = models.EmailField(unique=True, blank=False, null=False)
# 	created_by = models.ForeignKey(User, 
# 									on_delete=models.CASCADE, null=True,
# 									related_name='+')
# 	updated_by = models.ForeignKey(User, 
# 									on_delete=models.CASCADE, null=True,
# 									related_name='+')
# 	def __str__(self):
# 		return self.name

	# class Meta:
	# 	ordering = ['-created', ]




class Breakfast(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, related_name="breakfast")
	item_name = models.CharField(default="", blank=True, max_length=250)
	item_price = models.DecimalField(max_digits=6, decimal_places=2, default="")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="+")
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="+")

	def __str__(self):
		return self.item_name



class Dinner(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, related_name="dinner")
	item_name = models.CharField(max_length=255, default="")
	item_price = models.DecimalField(max_digits=6, decimal_places=2, default="")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
	
	class Meta:
		ordering = ['-created', ]


	def __str__(self):
		return self.item_name



	
	
class Lunch(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, related_name="lunch")
	item_name = models.CharField(max_length=255, default="")
	item_price = models.DecimalField(max_digits=6, decimal_places=2, default="")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')

	
	class Meta:
		ordering = ['-created', ]

	def __str__(self):
		return self.item_name

	


class Snacks(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, related_name="snacks")
	item_name = models.CharField(max_length=255, default="")
	item_price = models.DecimalField(max_digits=6, decimal_places=2, default="")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
	
	class Meta:
		ordering = ['-created', ]

	def __str__(self):
		return self.item_name

	

class TodaySpecial(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, related_name="today_special")
	item_name = models.CharField(max_length=255, default="")
	item_price = models.DecimalField(max_digits=6, decimal_places=2, default="")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')

	class Meta:
		ordering = ['-created', ]

	def __str__(self):
		return self.item_name

	
