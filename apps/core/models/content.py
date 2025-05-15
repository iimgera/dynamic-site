from django.db import models

from apps.users.models import Profile
from apps.core.enums import ContentType, ContentStatus


class Content(models.Model):
    class Meta:
        db_table = 'contents'
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'

    content_type = models.CharField(
        max_length=50,
        choices=ContentType.choices,
        help_text='Тип контента'
    )
    title = models.CharField(
        max_length=255,
        help_text='Заголовок'
    )
    body = models.JSONField(
        null=True,
        help_text='Содержание'
    )
    media_url = models.URLField(
        blank=True, null=True,
        help_text='Медиа'
    )
    status = models.CharField(
        max_length=50,
        choices=ContentStatus.choices,
        help_text='Статус'
    )
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL,
        null=True, help_text='Автор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Создано'
    )

    def __str__(self):
        return self.title
