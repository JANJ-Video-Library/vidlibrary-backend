# Generated by Django 3.1.1 on 2020-09-17 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_video_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.CharField(choices=[('Professional', 'Professional'), ('College', 'College'), ('Other', 'Other')], max_length=255),
        ),
    ]