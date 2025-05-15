from django.db import models
from apps.users.models import Profile


class Site(models.Model):
    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'
        db_table = 'sites'

    name = models.CharField(
        max_length=100,
        help_text='Название сайта',
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
    )
    created_by = models.ForeignKey(
        Profile, on_delete=models.SET_NULL,
        null=True, related_name='sites',
        help_text='Создано пользователем:'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Активен'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Создан:'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Изменен:'
    )

    def __str__(self):
        return self.name


class SiteSettings(models.Model):
    class Meta:
        db_table = 'site_settings'
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайтов'

    site = models.OneToOneField(
        Site, on_delete=models.CASCADE,
        related_name='settings',
        help_text='Сайт'
    )
    theme_colors = models.JSONField(
        help_text='Цвета темы'
    )
    fonts = models.JSONField(
        help_text='Шрифты'
    )
    logo = models.ImageField(
        upload_to='site_settings/logo',
        null=True, blank=True,
        help_text='Лого'
    )
    spacing = models.JSONField(
        help_text='Интервал'
    )

    def __str__(self):
        return f'Настройки сайта: {self.site.name}'
