from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			"id",
			"email",
			"contact_no",
			"first_name",
			"last_name",
			"gender",
			"is_active",
			# "created_at",
		]
