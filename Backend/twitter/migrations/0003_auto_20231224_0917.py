# Generated by Django 3.2.23 on 2023-12-24 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20231129_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Agent',
                'verbose_name_plural': 'Agents',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.DeleteModel(
            name='AccountRecord',
        ),
        migrations.DeleteModel(
            name='TwitterAccount',
        ),
        migrations.AddField(
            model_name='agent',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.project'),
        ),
    ]