# Generated by Django 3.2.7 on 2021-09-18 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Userr',
        ),
        migrations.RenameField(
            model_name='userr',
            old_name='address1',
            new_name='addressA',
        ),
        migrations.RenameField(
            model_name='userr',
            old_name='address2',
            new_name='addressB',
        ),
    ]