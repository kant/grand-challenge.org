# Generated by Django 2.1.2 on 2018-11-29 11:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cases", "0007_auto_20180909_0513"),
        ("patients", "0001_initial"),
        ("studies", "0001_initial"),
        ("worklists", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientItem",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients.Patient",
                    ),
                ),
                (
                    "study",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studies.Study",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="StudyItem",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cases.Image",
                    ),
                ),
                (
                    "study",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studies.Study",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="WorklistItem",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cases.Image",
                    ),
                ),
                (
                    "worklist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="worklists.Worklist",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]