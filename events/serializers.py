from rest_framework import serializers
from .models import *


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = (
			'__all__'
		)


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = (
			'__all__'
		)
