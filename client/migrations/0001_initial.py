# Generated by Django 4.2.9 on 2025-01-27 21:37

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
            name="Subscription",
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
                ("subscriber_name", models.CharField(max_length=300)),
                ("subscription_plan", models.CharField(max_length=255)),
                ("subscription_cost", models.CharField(max_length=255)),
                ("paypal_subscription_id", models.CharField(max_length=300)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        max_length=10,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
