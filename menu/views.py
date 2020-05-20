from django.shortcuts import render
from menu.models import Menu, Breakfast, TodaySpecial, Snacks, Lunch, Dinner
from menu.serializers import(
							MenuSerializer,
							BreakfastSerializer, 
							TodaySpecialSerializer, 
							SnacksSerializer, 
							LunchSerializer, 
							DinnerSerializer
						)

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (
		IsAuthenticated,
		AllowAny,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	) 
# Create your views here.

class MenuListCreateView(ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]

	ordering_fields = ['id',]

	search_fields = [
				'name', 
				'description',
			]

class MenuDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	permission_classes = [IsAdminUser,]

	ordering_fields = ['id',]
	
	search_fields = [
				'name', 
				'description',
			]




class BreakfastListView(ListCreateAPIView):
	queryset = Breakfast.objects.all()
	serializer_class = BreakfastSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]

	ordering_fields = ['id',]

	search_fields = [
				'item_name', 
				'item_price',
			]

class BreakfastDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Breakfast.objects.all()
	serializer_class = BreakfastSerializer
	permission_classes = [IsAdminUser,]

	ordering_fields = ['id',]
	
	search_fields = [
				'item_name', 
				'item_price',
			]




class DinnerListCreateView(ListCreateAPIView):
	queryset = Dinner.objects.all()
	serializer_class = DinnerSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]

	ordering_fields = ['id',]

	search_fields = [
				'item_name', 
				'item_price',
			]

class DinnerDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Dinner.objects.all()
	serializer_class = DinnerSerializer
	permission_classes = [IsAdminUser,]

	ordering_fields = ['id',]
	
	search_fields = [
				'item_name', 
				'item_price',
			]




class LunchListCreateView(ListCreateAPIView):
	queryset = Lunch.objects.all()
	serializer_class = LunchSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]

	ordering_fields = ['id',]

	search_fields = [
				'item_name', 
				'item_price',
			]

class LunchDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Lunch.objects.all()
	serializer_class = LunchSerializer
	permission_classes = [IsAdminUser,]

	ordering_fields = ['id',]
	
	search_fields = [
				'item_name', 
				'item_price',
			]




class SnacksListCreateView(ListCreateAPIView):
	queryset = Snacks.objects.all()
	serializer_class = SnacksSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]

	ordering_fields = ['id',]

	search_fields = [
				'item_name', 
				'item_price',
			]

class SnacksDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Snacks.objects.all()
	serializer_class = SnacksSerializer
	permission_classes = [IsAdminUser,]

	ordering_fields = ['id',]
	
	search_fields = [
				'item_name', 
				'item_price',
			]




class TodaySpecialListCreateView(ListCreateAPIView):
	queryset = TodaySpecial.objects.all()
	serializer_class = TodaySpecialSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]


	ordering_fields = ['id',]

	search_fields = [
				'item_name', 
				'item_price',
			]

class TodaySpecialDetailView(RetrieveUpdateDestroyAPIView):
	queryset = TodaySpecial.objects.all()
	serializer_class = TodaySpecialSerializer
	permission_classes = [IsAdminUser,]


	ordering_fields = ['id',]
	
	search_fields = [
				'item_name', 
				'item_price',
			]
