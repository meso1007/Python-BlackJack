# Generated by Django 5.1.7 on 2025-03-17 07:45

import blackjack.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GameSession",
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
                ("player_hand", models.JSONField(default=list)),
                ("dealer_hand", models.JSONField(default=list)),
                ("deck", models.JSONField(default=blackjack.models.create_deck)),
                ("game_over", models.BooleanField(default=False)),
                ("winner", models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
