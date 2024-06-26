# Generated by Django 5.0.1 on 2024-02-09 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('slika', models.ImageField(upload_to='slike/')),
                ('opis', models.TextField(blank=True)),
                ('kategorija', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
