# Generated by Django 3.2.7 on 2021-09-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_userr_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='addressA',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='addressB',
            field=models.CharField(max_length=50),
        ),
    ]
