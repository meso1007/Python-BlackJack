# Generated by Django 5.1.7 on 2025-03-17 09:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blackjack", "0002_card"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Card",
        ),
    ]
