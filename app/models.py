from django.db import models

class Cartas(models.Model):
    cartas_nome = models.CharField(max_length=100,default='a')
    cartas_descricao = models.CharField(max_length=1000,default='a')
    cartas_atk = models.IntegerField(default=1)
    cartas_def = models.IntegerField(default=1)

    def __str__(self):
        return self.cartas_nome

    