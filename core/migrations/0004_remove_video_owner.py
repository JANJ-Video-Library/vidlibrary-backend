# Generated by Django 3.1.1 on 2020-09-17 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200917_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='owner',
        ),
    ]
