from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Membro(models.Model):
    nome = models.CharField(max_length=20)
    #descrizione = models.TextField()
    descrizione = RichTextField(null=True,blank=True)

    def __str__(self):
        return self.nome
