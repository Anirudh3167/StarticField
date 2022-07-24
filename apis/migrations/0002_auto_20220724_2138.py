# Generated by Django 3.2.6 on 2022-07-24 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_event_usereventmap'),
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='usereventmap',
            name='event',
        ),
        migrations.RemoveField(
            model_name='usereventmap',
            name='user',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='UserEventMap',
        ),
    ]
