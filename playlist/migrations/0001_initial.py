# Generated by Django 4.1.7 on 2023-04-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VibeCheck",
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
                ("artist1", models.CharField(max_length=50)),
                ("artist2", models.CharField(max_length=50)),
                ("artist3", models.CharField(max_length=50)),
                ("artist4", models.CharField(max_length=50)),
                ("artist5", models.CharField(max_length=50)),
            ],
        ),
    ]