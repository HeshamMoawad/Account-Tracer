# Generated by Django 3.2.23 on 2023-12-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0008_auto_20231225_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountlogininfo',
            name='profileImgURL',
            field=models.CharField(default='', max_length=200, verbose_name='ImgURL'),
            preserve_default=False,
        ),
    ]
