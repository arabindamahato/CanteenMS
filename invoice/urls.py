from django.urls import path
from invoice import views

urlpatterns = [
		path('', views.InvoiceList.as_view()),
		path('<pk>/', views.InvoiceDetail.as_view()),
]