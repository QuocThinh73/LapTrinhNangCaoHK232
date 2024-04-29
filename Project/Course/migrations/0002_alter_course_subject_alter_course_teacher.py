# Generated by Django 5.0.4 on 2024-04-29 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Course", "0001_initial"),
        ("Databases", "0003_major_department"),
        ("Teacher", "0004_degrees_teacher_teaching_schedule_teacher_degrees"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Databases.subject",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="teacher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Teacher.teacher",
            ),
        ),
    ]
