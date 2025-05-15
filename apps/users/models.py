from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    class Meta:
        db_table = 'roles'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    name = models.CharField(
        max_length=50,
        help_text='Наименование роли',
        unique=True
    )

    def __str__(self):
        return self.name


class Profile(models.Model):
    class Meta:
        db_table = 'profiles'
        verbose_name = 'Профили'
        verbose_name_plural = 'Профили'

    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        help_text='Пользователь',
        related_name='profile',
    )
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL,
        null=True, help_text='Роль'
    )
    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        blank=True,
        help_text='Фотография профиля'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Создан'
    )

    def __str__(self):
        return self.user.get_full_name()
