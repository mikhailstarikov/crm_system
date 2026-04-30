from django.db import models

from contracts.models import Contract
from leads.models import Lead


class ActiveClient(models.Model):
    """Активный клиент (создается из потенциального)"""

    lead = models.OneToOneField(
        Lead, on_delete=models.PROTECT, verbose_name="Потенциальный клиент"
    )
    contract = models.OneToOneField(
        Contract, on_delete=models.PROTECT, verbose_name="Контракт"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата конверсии")

    def __str__(self):
        return f"Активный клиент: {self.lead.name}"

    class Meta:
        verbose_name = "Активный клиент"
        verbose_name_plural = "Активные клиенты"
