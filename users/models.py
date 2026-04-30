from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Пользователь с ролью для CRM"""

    ROLE_CHOICES = (
        ("admin", "Администратор"),
        ("operator", "Оператор"),
        ("marketer", "Маркетолог"),
        ("manager", "Менеджер"),
    )

    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default="operator", verbose_name="Роль"
    )

    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
