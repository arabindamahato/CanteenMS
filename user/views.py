from django.shortcuts import render
from user.models import User
from user.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
		IsAuthenticated,
		AllowAny,
		IsAdminUser,
	) 
from user.permissions import (
		IsLoggedInUserOrAdmin,
		IsLoggedInUser,
		IsAdminUser,
		# IsGetOrPatchOrPut,
	) 

# Create your views here.

class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	# permission_classes = [IsAdminUser,]
	
	def get_permissions(self):
		permission_classes = []
		if self.action == 'create':
			permission_classes = [AllowAny]
		elif self.action == 'retrieve':
			permission_classes = [IsAdminUser]
		elif self.action == 'update' or self.action == 'partial_update':
			permission_classes = [IsLoggedInUserOrAdmin]
		elif  self.action == 'list' or self.action == 'destroy':
			permission_classes = [IsAdminUser]
		return [permission() for permission in permission_classes]




	search_fields = ('first_name','email','contact_no','last_name')
	ordering_fields = ('id',)