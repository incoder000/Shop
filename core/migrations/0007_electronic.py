# Generated by Django 4.1.6 on 2023-04-27 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_home_remove_user_is_verified_user_password_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Electronic",
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
                ("title", models.CharField(max_length=50)),
            ],
        ),
    ]
