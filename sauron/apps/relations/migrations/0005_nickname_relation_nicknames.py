# Generated by Django 4.1.1 on 2022-09-11 21:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        (
            "relations",
            "0004_remove_attachment_relation_remove_link_relation_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Nickname",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("note", models.TextField(blank=True)),
                ("nickname", models.TextField(blank=True, max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name="relation",
            name="nicknames",
            field=models.ManyToManyField(blank=True, to="relations.nickname"),
        ),
    ]