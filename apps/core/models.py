from django.db import models

# Create your models here.
class listbanks(models.Model):

    cod_compensacao = models.PositiveSmallIntegerField('Código de Compensação', primary_key=True, unique=True)
    nome_instituicao = models.CharField('Nome da Instituição', max_length=150)

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
        ordering = ['cod_compensacao']

    def __str__(self):
        return self.nome_instituicao
