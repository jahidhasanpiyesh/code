# Generated by Django 4.2.5 on 2023-09-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('collage', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('skill', models.TextField(max_length=200)),
                ('about_you', models.TextField(max_length=500)),
                ('previews_work', models.TextField(max_length=300)),
            ],
        ),
    ]
