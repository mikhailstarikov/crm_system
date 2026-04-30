from django.db import models


class Service(models.Model):
    """Услуга компании"""

    name = models.CharField(max_length=255, unique=True, verbose_name="Название услуги")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Стоимость"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    @property
    def cost(self):
        return self.price

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["name"]
