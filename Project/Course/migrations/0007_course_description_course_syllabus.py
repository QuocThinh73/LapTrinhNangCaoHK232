# Generated by Django 5.0.4 on 2024-05-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0006_course_course_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='syllabus',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
