# Generated by Django 2.1.7 on 2022-09-15 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='id_dominio',
            field=models.CharField(default='', max_length=8),
        ),
    ]