from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'is_staff', 'is_superuser'
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password',)
        }),
        ('Personal info', {
            'fields': ('email',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('email',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
