# Generated by Django 2.0 on 2020-03-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0002_auto_20200322_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='comments',
            field=models.CharField(blank=True, max_length=500, verbose_name='Комментарии'),
        ),
    ]
