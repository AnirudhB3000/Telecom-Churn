# Generated by Django 4.1 on 2023-01-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_delete_mlmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reviews",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("PlaintextReviews", models.TextField(max_length=500)),
                ("PosFeedback", models.FloatField(max_length=50)),
                ("NegFeedback", models.FloatField(max_length=50)),
                ("Alt", models.FloatField(max_length=50)),
            ],
        ),
    ]
