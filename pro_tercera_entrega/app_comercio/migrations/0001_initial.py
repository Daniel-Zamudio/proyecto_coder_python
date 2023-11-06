# Generated by Django 4.2.6 on 2023-11-01 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('mayorista', models.BooleanField(default=False)),
                ('dni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['apellido'],
            },
        ),
    ]
