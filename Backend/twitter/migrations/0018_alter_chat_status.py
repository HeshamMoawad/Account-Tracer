# Generated by Django 3.2.23 on 2024-01-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0017_auto_20240114_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='status',
            field=models.CharField(max_length=50, verbose_name='Status'),
        ),
    ]
