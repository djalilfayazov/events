from django.contrib import admin
from .models import *


from .forms import *
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('id', 'email', 'username', 'firstname', 'lastname')
    list_display_links = ('username',)

    fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'fields': ('firstname', 'lastname',)
            }
        ),
    )


    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                'fields': ('firstname', 'lastname',)
            }
        ),
    )

    ordering = ('id',)



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start', 'finish')
    list_display_links = ('id', 'name')
