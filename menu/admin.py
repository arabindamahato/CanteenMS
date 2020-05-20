from django.contrib import admin
from menu.models import Menu, Breakfast, TodaySpecial, Snacks, Lunch, Dinner

admin.site.site_header = "Canteen Management System"

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
	list_display = [
			'name',
			'description',
			
		]
	list_per_page = 4


	list_display_links = ['name','description']

	# list_editable = ['name',]

	search_fields = ['name', 'description']

	list_filter = ['name',]

	fields = [
		# while creating user these field comes
		'name',
		'description',
		'is_active',
		
	]



admin.site.register(Menu, MenuAdmin)



class BreakfastAdmin(admin.ModelAdmin):
	list_display = [
			'menu',
			'item_name',
			'item_price',
			'created',
			'is_active',
			# 'created_by',
		]
	list_per_page = 5


	list_display_links = ['item_name', 'menu']

	list_editable = ['item_price',]

	search_fields = ['item_name',]

	list_filter = ['item_name',]

	fields = [
		# while creating user these field comes
		'item_name',
		'item_price',
		'menu',
	]

admin.site.register(Breakfast, BreakfastAdmin)



class DinnerAdmin(admin.ModelAdmin):
	list_display = [
			'item_name',
			'item_price',
			'created',
			'is_active',
			'created_by',
			'menu',
		]
	list_per_page = 5


	list_display_links = ['item_name','menu']

	list_editable = ['item_price',]

	search_fields = ['item_name',]

	list_filter = ['item_name',]

	fields = [
		# while creating user these field comes
		'item_name',
		'item_price',
		'menu',
	]

admin.site.register(Dinner, DinnerAdmin)



class LunchAdmin(admin.ModelAdmin):
	list_display = [
			'item_name',
			'item_price',
			'created',
			'is_active',
			'created_by',
			'menu',
		]
	list_per_page = 5


	list_display_links = ['item_name', 'menu']

	list_editable = ['item_price',]

	search_fields = ['item_name',]

	list_filter = ['item_name',]

	fields = [
		# while creating user these field comes
		'item_name',
		'item_price',
		'menu',
	]

admin.site.register(Lunch, LunchAdmin)




class SnacksAdmin(admin.ModelAdmin):
	list_display = [
			'item_name',
			'item_price',
			'created',
			'is_active',
			'created_by',
			'menu',
		]
	list_per_page = 4


	list_display_links = ['item_name', 'menu']

	list_editable = ['item_price',]

	search_fields = ['item_name',]

	list_filter = ['item_name',]

	fields = [
		# while creating user these field comes
		'item_name',
		'item_price',
		'menu',
	]

admin.site.register(Snacks, SnacksAdmin)



class TodaySpecialAdmin(admin.ModelAdmin):
	list_display = [
			'item_name',
			'item_price',
			'created',
			'is_active',
			'created',
			'menu',
		]
	list_per_page = 4


	list_display_links = ['item_name', 'menu',]

	list_editable = ['item_price',]

	search_fields = ['item_name',]

	list_filter = ['item_name',]

	fields = [
		# while creating user these field comes
		'item_name',
		'item_price',
		'menu',
	]
admin.site.register(TodaySpecial, TodaySpecialAdmin) 
