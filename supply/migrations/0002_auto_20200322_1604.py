# Generated by Django 2.0 on 2020-03-22 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('supply', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedpythback',
            new_name='Feedback',
        ),
    ]