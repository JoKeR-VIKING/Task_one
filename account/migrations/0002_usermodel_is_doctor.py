# Generated by Django 4.1.5 on 2023-01-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_doctor',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
