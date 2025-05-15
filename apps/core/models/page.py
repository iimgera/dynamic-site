from django.db import models

from apps.core.enums import BlockType
from apps.core.models.site import Site


class Page(models.Model):
    class Meta:
        db_table = 'pages'
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    title = models.CharField(
        max_length=255,
        help_text="Заголовок страницы",
    )
    institution = models.ForeignKey(
        Site, on_delete=models.SET_NULL,
        null=True, blank=True,
        help_text='Учреждение'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        help_text='Порядок в меню'
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


class Block(models.Model):
    class Meta:
        db_table = 'blocks'
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    page = models.ForeignKey(
        Page, on_delete=models.CASCADE,
        related_name='blocks',
        help_text='Страница'
    )
    block_type = models.CharField(
        max_length=255,
        choices=BlockType.choices,
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        help_text='Порядок'
    )
    settings = models.JSONField(
        help_text='Настройки'
    )

    def __str__(self):
        return self.block_type
