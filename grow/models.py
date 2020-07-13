from django.db import models

from core.models import TimeStampedModel, Active


class Lampada(Active, TimeStampedModel):
    pin = models.IntegerField('Pino')
    name = models.CharField(max_length=100)
    time_on = models.TimeField('Ligar as')
    time_off = models.TimeField('Desligar as')


class Relay(Active, TimeStampedModel):
    pin = models.IntegerField('Pino')
    name = models.CharField(max_length=100)
