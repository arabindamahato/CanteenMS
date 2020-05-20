from django.shortcuts import render
from rest_framework import generics
from invoice.serializers import InvoiceSerializer
from invoice.models import Invoice
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.


class InvoiceList(generics.ListCreateAPIView):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceSerializer
	permission_classes = [IsAuthenticated,]

	ordering_fields = '__all__'

	search_fields = [
			'invoice_number',
			'date_of_issue',
			'total_price'
		]


class InvoiceDetail(generics.RetrieveUpdateAPIView):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceSerializer
	permission_classes = [IsAuthenticated,]

	ordering_fields = '__all__'

	search_fields = [
			'invoice_number',
			'date_of_issue',
			'total_price'
		]
