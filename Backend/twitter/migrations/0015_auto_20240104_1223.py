# Generated by Django 3.2.23 on 2024-01-04 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0014_auto_20240102_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Media URL')),
                ('type', models.CharField(choices=[('video', 'Video'), ('image', 'Image')], default='image', max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'Chat', 'verbose_name_plural': 'Chats'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name': 'Reply', 'verbose_name_plural': 'Replies'},
        ),
        migrations.AddField(
            model_name='reply',
            name='media_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Media URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accountlogininfo',
            name='profileImgURL',
            field=models.URLField(verbose_name='ImgURL'),
        ),
        migrations.AddField(
            model_name='reply',
            name='media_links',
            field=models.ManyToManyField(blank=True, to='twitter.MediaLink'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='media_links',
            field=models.ManyToManyField(blank=True, to='twitter.MediaLink'),
        ),
    ]
