# Generated by Django 3.0.1 on 2019-12-21 22:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20191221_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='descrizione',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Code'),
        ),
    ]
