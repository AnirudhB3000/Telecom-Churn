# Generated by Django 4.1 on 2023-01-29 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_rename_review_churn_alt_alter_reviews_alt"),
    ]

    operations = [
        migrations.RenameField(model_name="churn", old_name="Alt", new_name="Review",),
    ]
