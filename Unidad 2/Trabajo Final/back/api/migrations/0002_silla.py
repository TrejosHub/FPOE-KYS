# Generated by Django 5.0.3 on 2024-03-22 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Silla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.TextField(blank=True, max_length=5000)),
                ('altura', models.FloatField(blank=True, max_length=5000)),
                ('peso', models.FloatField(blank=True, max_length=5000)),
                ('estilo', models.TextField(blank=True, max_length=5000)),
            ],
        ),
    ]
