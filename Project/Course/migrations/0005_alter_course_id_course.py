# Generated by Django 5.0.4 on 2024-04-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Course", "0004_alter_course_id_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="id_course",
            field=models.CharField(max_length=3, null=True),
        ),
    ]
