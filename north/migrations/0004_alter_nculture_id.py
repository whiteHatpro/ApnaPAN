# Generated by Django 4.1.3 on 2022-11-05 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("north", "0003_remove_nculture_man_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nculture",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
