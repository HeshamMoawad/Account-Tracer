# Generated by Django 3.2.23 on 2024-01-02 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0013_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountlogininfo',
            name='id_str',
        ),
        migrations.AlterField(
            model_name='accountlogininfo',
            name='screen_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Screen Name'),
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='handle',
            field=models.CharField(max_length=50, unique=True, verbose_name='Handle'),
        ),
    ]
