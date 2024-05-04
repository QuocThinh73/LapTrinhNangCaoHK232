# Generated by Django 5.0.4 on 2024-05-03 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assessment', '0001_initial'),
        ('Course', '0011_merge_20240503_1814'),
        ('Student', '0012_rename_id_student_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_feedback', models.TextField()),
                ('teacher_feedback', models.TextField()),
                ('improvements', models.TextField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Course.course')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.student')),
            ],
        ),
    ]