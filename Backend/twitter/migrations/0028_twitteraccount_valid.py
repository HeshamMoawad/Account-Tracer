# Generated by Django 3.2.23 on 2024-01-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0027_auto_20240122_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteraccount',
            name='valid',
            field=models.BooleanField(default=True, verbose_name='IsValid'),
        ),
    ]
