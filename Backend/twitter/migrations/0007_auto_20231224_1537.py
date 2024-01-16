# Generated by Django 3.2.23 on 2023-12-24 13:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0006_project_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date'),
        ),
        migrations.AddField(
            model_name='agent',
            name='updated_datetime',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date'),
        ),
        migrations.AddField(
            model_name='project',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updated_datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.CreateModel(
            name='TwitterAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=50, verbose_name='Handle')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('updated_datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.agent')),
            ],
            options={
                'verbose_name': 'Twitter Account',
                'verbose_name_plural': 'Twitter Accounts',
            },
        ),
        migrations.CreateModel(
            name='AccountLoginInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_str', models.CharField(max_length=50, unique=True, verbose_name='ID')),
                ('rest_id', models.CharField(max_length=50, verbose_name='Rest ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('description', models.TextField(max_length=300, verbose_name='Bio')),
                ('screen_name', models.CharField(max_length=50, null=True, verbose_name='Handle')),
                ('verified', models.BooleanField(default=False, verbose_name='Verified')),
                ('cookies', models.CharField(max_length=500, verbose_name='Cookies')),
                ('token', models.CharField(max_length=300, verbose_name='Token')),
                ('suspend', models.BooleanField(default=False, verbose_name='Suspension Status')),
                ('created_at', models.CharField(max_length=60, verbose_name='Created At')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_datetime', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.twitteraccount')),
            ],
            options={
                'verbose_name': 'Account Login Info',
                'verbose_name_plural': 'Accounts Login Info',
            },
        ),
    ]