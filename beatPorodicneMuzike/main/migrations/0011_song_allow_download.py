# Generated by Django 5.0.1 on 2024-02-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='allow_download',
            field=models.BooleanField(default=True),
        ),
    ]
