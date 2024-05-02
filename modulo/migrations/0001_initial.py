# Generated by Django 5.0.4 on 2024-05-02 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dni", models.CharField(max_length=15, unique=True)),
                ("nombre", models.CharField(max_length=100)),
                ("direccion", models.CharField(blank=True, max_length=255, null=True)),
                ("telefono", models.CharField(blank=True, max_length=15, null=True)),
                ("correo", models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]