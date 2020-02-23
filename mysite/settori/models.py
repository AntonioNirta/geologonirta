from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Settore(models.Model):
    titolo = models.CharField(max_length=250)
    descrizione = RichTextField(null=True,blank=True)

    def __str__(self):
        return self.titolo
