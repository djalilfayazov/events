from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('events.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('registration/', include('dj_rest_auth.registration.urls')),
]
