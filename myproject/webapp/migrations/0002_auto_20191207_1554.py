# Generated by Django 2.2.7 on 2019-12-07 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='firstnaeme',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='lastnaeme',
            new_name='lastname',
        ),
    ]
