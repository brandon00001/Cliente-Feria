from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
# Create your models here.

class UserSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	first_name = serializers.CharField()
	last_name = serializers.CharField()
	username = serializers.CharField()
	email = serializers.EmailField()
	password = serializers.CharField()

	def create(self, validate_data):
		payload = {"first_name": validate_data.get('first_name'),
			   "last_name": validate_data.get('last_name'),
			   "username": validate_data.get('username'),
			   "email": validate_data.get('email'),
			   "password": validate_data.get('password')
			   }
		r = requests.post('http://letalisumbra.pythonanywhere.com/api/1.0/create_user/', json=payload)
		return r.text

	def __str__(self):
		return self.username