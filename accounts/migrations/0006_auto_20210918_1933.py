# Generated by Django 3.2.7 on 2021-09-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210918_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='addressA',
        ),
        migrations.RemoveField(
            model_name='user',
            name='addressB',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
    ]
