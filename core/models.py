from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    describe = models.TextField(blank=True, null=True)
    dt_event = models.DateTimeField(verbose_name='Data do Evento')
    dt_creation = models.DateTimeField(auto_now=True, verbose_name='Data de Criacao')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'

    def __str__(self):
        return self.title