from rest_framework import serializers
from menu.models import (
				Menu, 
				Breakfast, 
				TodaySpecial, 
				Lunch, 
				Snacks, 
				Dinner
)




		



class BreakfastSerializer(serializers.ModelSerializer):
	class Meta:
		model = Breakfast
		fields = [
			'id', 
			'item_name',
			'item_price',
		]

		read_only_fields = ["id", "is_active"]


class DinnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dinner
		fields = [
			'id', 
			'item_name',
			'item_price',
		]

		read_only_fields = ["id", "is_active"]



class LunchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lunch
		fields = [
			'id', 
			'item_name',
			'item_price',
		]

		read_only_fields = ["id", "is_active"]



class SnacksSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Snacks
		fields = [
			'id', 
			'item_name',
			'item_price',
		]

		read_only_fields = ["id", "is_active"]



class TodaySpecialSerializer(serializers.ModelSerializer):
	class Meta:
		model = TodaySpecial
		fields = [
			'id', 
			'item_name',
			'item_price',
		]

		read_only_fields = ["id", "is_active"]



class MenuSerializer(serializers.ModelSerializer):
	breakfast = BreakfastSerializer(read_only=True, many=True)
	today_special = TodaySpecialSerializer(read_only=True, many=True)
	lunch = LunchSerializer(read_only=True, many=True)
	snacks = SnacksSerializer(read_only=True, many=True)
	dinner = DinnerSerializer(read_only=True, many=True)
	class Meta:
		model = Menu
		fields = [
			'id', 
			'name',
			'description',
			'breakfast',
			'today_special',
			'lunch',
			'snacks',
			'dinner',
		]

		read_only_fields = ["id", "is_active"]

