# Generated by Django 5.0.3 on 2024-05-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_papitas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papitas',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='papitas',
            name='marca',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]