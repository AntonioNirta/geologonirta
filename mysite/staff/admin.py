from django.contrib import admin
from ckeditor.fields import RichTextField
from .models import Membro

#Register your models here.

admin.site.register(Membro)
