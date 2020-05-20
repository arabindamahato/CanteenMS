from django.urls import path
from menu.views import ( 
				MenuListCreateView, 
				MenuDetailView, 
				BreakfastListView, 
				BreakfastDetailView, 
				DinnerListCreateView, 
				DinnerDetailView, 
				LunchListCreateView, 
				LunchDetailView, 
				SnacksListCreateView, 
				SnacksDetailView, 
				TodaySpecialListCreateView, 
				TodaySpecialDetailView,
		)

urlpatterns = [
	path('', MenuListCreateView.as_view()),
	path('<pk>/', MenuDetailView.as_view()),

	path('breakfast', BreakfastListView.as_view()),
	path('breakfast/<pk>/', BreakfastDetailView.as_view()),

	path('dinner', DinnerListCreateView.as_view()),
	path('dinner/<pk>/', DinnerDetailView.as_view()),

	path('snacks', SnacksListCreateView.as_view()),
	path('snacks/<pk>/', SnacksDetailView.as_view()),

	path('today-special', TodaySpecialListCreateView.as_view()),
	path('today-special/<pk>/', TodaySpecialDetailView.as_view()),

	path('lunch', LunchListCreateView.as_view()),
	path('lunch/<pk>/', LunchDetailView.as_view()),
]