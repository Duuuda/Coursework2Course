from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50, unique=True)
    balance = models.DecimalField(verbose_name='Money', max_digits=20, decimal_places=2, default=0)

    @property
    def human_view(self) -> str:
        return f'Client id: {self.id}\n' \
               f'Client name: {self.name}\n' \
               f'Client balance: {self.balance}\n'

    def __str__(self) -> str:
        return f'<Client("{self.name}")>'

    class Meta:
        verbose_name = "Bank's Client"
        verbose_name_plural = "Bank's Clients"
