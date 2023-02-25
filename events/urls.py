from django.urls import path
from .views import *


urlpatterns = [
	path('', EventList.as_view(), name='api'),
	path('event-<int:pk>/', EventDetail.as_view())
]
