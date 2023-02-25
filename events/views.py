from .models import *
from rest_framework import generics
from .serializers import *
from .permissions import *
from rest_framework import permissions


class EventList(generics.ListCreateAPIView):
	permission_classes = (IsOwnerOrReadOnly, )
	queryset = Event.objects.all()
	serializer_class = EventSerializer



class EventDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAdminUser,)
	queryset = Event.objects.all()
	serializer_class = EventSerializer
