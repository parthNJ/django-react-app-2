# Generated by Django 3.1 on 2020-08-20 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_userprogram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='modules',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]
