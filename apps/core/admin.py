from django.contrib import admin

from apps.core.models.site import Site, SiteSettings
from apps.core.models.content import Content
from apps.core.models.page import Page, Block
from apps.core.models.moderation import Moderation


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'created_by',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'created_by',
        'created_at',
        'is_active',
    )


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'site',
        'theme_colors',
        'fonts',
        'logo',
        'spacing'
    )


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content_type',
        'title',
        'body',
        'media_url',
        'status',
        'author',
        'created_at',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'content_type',
        'status',
        'author',
    )


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'institution',
        'slug',
        'order',
        'is_active'
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'institution',
        'slug',
        'order',
        'is_active'
    )


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'page',
        'block_type',
        'order',
        'settings'
    )
    list_filter = (
        'page',
        'block_type',
        'order',
    )


@admin.register(Moderation)
class ModerationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
        'status',
        'moderated_by',
        'comment',
        'moderated_at'
    )
    list_filter = (
        'content',
        'status',
        'moderated_by',
    )
