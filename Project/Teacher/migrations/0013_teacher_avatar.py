# Generated by Django 5.0.4 on 2024-05-03 23:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Teacher", "0012_teacher_hometown"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="Avatar/Teacher/"),
        ),
    ]