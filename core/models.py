from django.db import models


class Pessoa(models.Model):
    objects = None
    nome = models.CharField('nome', max_length=250)
    email = models.CharField('email', max_length=120)
    data_nascimento = models.DateField('Data de nascimento')

    class Meta:
        ordering = ('nome',)
