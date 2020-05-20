from django.contrib import admin
from user.models import User
from django.contrib.auth.models import Group

admin.site.site_header = "Canteen Management System"
	# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = [
		'email', 'firstname_and_lastname', 'contact_no',
		'is_admin', 'is_active', 'is_staff', 'is_superuser']
		
	list_per_page = 5

	list_display_links = ['email',]

	list_editable = ['contact_no',]

	search_fields = ['first_name', 'email']

	list_filter = ['is_admin',]

	fields = [
		# while creating user these field comes
		'email',
		'contact_no',
		'first_name',
		'last_name',
		'password',
	]

	def firstname_and_lastname(self, obj): 
		return "{}  {}".format(obj.first_name, obj.last_name)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
