# Generated by Django 5.0.4 on 2024-04-24 16:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Student", "0008_student_department_student_major"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="major",
        ),
    ]