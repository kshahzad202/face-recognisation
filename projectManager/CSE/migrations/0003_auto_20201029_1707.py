# Generated by Django 3.1.1 on 2020-10-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0002_auto_20201029_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstsemester',
            name='UPLOAD',
        ),
        migrations.AlterField(
            model_name='firstsemester',
            name='images',
            field=models.FileField(blank=True, max_length=50, upload_to='firstYear'),
        ),
    ]
