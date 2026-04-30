from django.db import models

from ads.models import AdvertisingCampaign


class Lead(models.Model):
    """Потенциальный клиент"""

    first_name = models.CharField(max_length=100, default="", verbose_name="Имя")
    last_name = models.CharField(max_length=100, default="", verbose_name="Фамилия")

    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")

    campaign = models.ForeignKey(
        AdvertisingCampaign,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads",
        verbose_name="Рекламная кампания",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Потенциальный клиент"
        verbose_name_plural = "Потенциальные клиенты"
