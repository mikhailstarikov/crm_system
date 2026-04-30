from django.db import models

from services.models import Service


class AdvertisingCampaign(models.Model):
    """Рекламная кампания"""

    name = models.CharField(max_length=255, verbose_name="Название кампании")
    product = models.ForeignKey(
        Service, on_delete=models.CASCADE, verbose_name="Рекламируемая услуга"
    )
    channel = models.CharField(max_length=100, verbose_name="Канал продвижения")
    budget = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Бюджет на рекламу"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Рекламная кампания"
        verbose_name_plural = "Рекламные кампании"
        ordering = ["-created_at"]
