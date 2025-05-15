from django.db import models

from apps.users.models import Profile
from .content import Content
from apps.core.enums import ModerationStatus


class Moderation(models.Model):
    class Meta:
        db_table = 'moderations'
        verbose_name = 'Модерация'
        verbose_name_plural = 'Модерации'

    content = models.ForeignKey(
        Content, on_delete=models.CASCADE,
        related_name='moderations',
        help_text='Контент'
    )
    status = models.CharField(
        max_length=20,
        choices=ModerationStatus.choices,
        default=ModerationStatus.PENDING,
        help_text='Статус'
    )
    moderated_by = models.ForeignKey(
        Profile, on_delete=models.SET_NULL,
        related_name='moderated_by',
        null=True
    )
    comment = models.TextField(
        blank=True, help_text='Комментарий'
    )
    moderated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.content
