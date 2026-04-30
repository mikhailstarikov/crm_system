from django.db import models

from services.models import Service


class Contract(models.Model):
    """Контракт с клиентом"""

    name = models.CharField(max_length=255, verbose_name="Название контракта")
    service = models.ForeignKey(
        Service, on_delete=models.PROTECT, verbose_name="Услуга"
    )
    document = models.FileField(
        upload_to="contracts/", null=True, blank=True, verbose_name="Документ (файл)"
    )
    date_signed = models.DateField(verbose_name="Дата заключения")
    period = models.CharField(max_length=100, verbose_name="Период действия")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    @property
    def product(self):
        return self.service

    @property
    def start_date(self):
        return self.date_signed

    @property
    def end_date(self):
        return self.period

    @property
    def cost(self):
        return self.amount

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
