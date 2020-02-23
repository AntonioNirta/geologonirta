from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Lavoro(models.Model):
    committente = models.CharField(max_length=250)
    titolo = models.CharField(max_length=250)
    anno = models.IntegerField()

    def __str__(self):
        return self.titolo
