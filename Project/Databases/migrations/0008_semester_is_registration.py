# Generated by Django 5.0.4 on 2024-04-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Databases", "0007_semester_semester_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="semester",
            name="is_registration",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
