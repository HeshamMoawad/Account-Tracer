# Generated by Django 3.2.23 on 2023-12-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_auto_20231224_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='imgURL',
            field=models.ImageField(null=True, upload_to='projectsAssets/'),
        ),
    ]
