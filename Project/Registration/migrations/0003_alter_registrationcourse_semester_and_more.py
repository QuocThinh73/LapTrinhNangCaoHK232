# Generated by Django 5.0.4 on 2024-04-29 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Databases", "0007_semester_semester_id"),
        ("Registration", "0002_registrationcourse_semester"),
        ("Student", "0011_alter_student_major"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registrationcourse",
            name="semester",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Databases.semester",
            ),
        ),
        migrations.AlterField(
            model_name="registrationcourse",
            name="student",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Student.student",
            ),
        ),
        migrations.AlterField(
            model_name="registrationcourse",
            name="subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Databases.subject",
            ),
        ),
    ]
