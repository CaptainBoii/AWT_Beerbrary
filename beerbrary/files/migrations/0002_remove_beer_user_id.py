# Generated by Django 4.0.4 on 2022-05-25 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer',
            name='user_id',
        ),
    ]
