# Generated by Django 3.2.12 on 2024-05-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0002_alter_student_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_total',
            field=models.IntegerField(max_length=10),
        ),
    ]
