# Generated by Django 4.2.2 on 2023-06-21 05:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("publication_date", models.DateField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("is_available", models.BooleanField(default=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("description", models.TextField()),
                ("book_code", models.CharField(max_length=20)),
                ("category", models.CharField(max_length=50)),
                ("genre", models.CharField(max_length=50)),
                ("rating", models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]
