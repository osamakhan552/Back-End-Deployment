# Generated by Django 3.2.7 on 2022-11-06 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='createdBy',
        ),
    ]
