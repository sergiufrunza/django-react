from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name",)}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
