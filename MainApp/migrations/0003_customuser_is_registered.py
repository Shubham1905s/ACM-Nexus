# Generated by Django 5.0 on 2023-12-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
    ]
