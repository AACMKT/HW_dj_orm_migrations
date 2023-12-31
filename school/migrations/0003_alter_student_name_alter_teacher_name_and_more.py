# Generated by Django 4.2.4 on 2023-08-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0002_remove_student_teacher_alter_student_group_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="name",
            field=models.CharField(max_length=64, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="name",
            field=models.CharField(max_length=64, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="subject",
            field=models.CharField(max_length=64, verbose_name="Предмет"),
        ),
    ]
