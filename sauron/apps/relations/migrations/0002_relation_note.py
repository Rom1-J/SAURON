# Generated by Django 4.1.1 on 2022-09-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("relations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="relation",
            name="note",
            field=models.TextField(blank=True),
        ),
    ]
