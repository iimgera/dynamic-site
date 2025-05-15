from django.contrib import admin
from apps.users.models import Profile, Role


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'role',
        'profile_picture',
        'created_at'
    )
    search_fields = (
        'user__username',
        'role',
        'user__first_name',
        'user__last_name',
    )
    list_filter = (
        'role',
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
