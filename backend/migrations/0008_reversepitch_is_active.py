# Generated by Django 3.2.6 on 2022-07-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_rename_program_reversepitch'),
    ]

    operations = [
        migrations.AddField(
            model_name='reversepitch',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
