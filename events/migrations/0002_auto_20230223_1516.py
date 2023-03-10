# Generated by Django 3.2 on 2023-02-23 10:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='invited',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='finish',
            field=models.DateTimeField(verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(verbose_name='Начало'),
        ),
        migrations.DeleteModel(
            name='Invited',
        ),
    ]
