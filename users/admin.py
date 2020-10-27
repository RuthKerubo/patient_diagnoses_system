from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdminCustom(UserAdmin):

    list_display = ('email', 'id_no', 'first_name', 'surname', 'is_staff',)
    list_filter = ('is_staff',)
    # Displayed when updating
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'surname', 'id_no')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    # Displayed when creating a new user
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'first_name', 'surname', 'id_no',
                    'password1', 'password2'
                )
            }
        ),
    )
    search_fields = ('email', 'first_name', 'surname', 'id_no')
    ordering = ('email', 'first_name', 'surname', 'id_no')
    filter_horizontal = ()


admin.site.register(User, UserAdminCustom)
