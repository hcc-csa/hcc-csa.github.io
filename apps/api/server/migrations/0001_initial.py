# Generated by Django 5.0.3 on 2024-04-19 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('website', models.URLField()),
                ('github', models.URLField()),
                ('discord', models.URLField()),
                ('linkedid', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('event_date', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('address', models.CharField(max_length=100)),
                ('registration_link', models.URLField()),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='media_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.media'),
        ),
        migrations.CreateModel(
            name='Officials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(choices=[('P1', 'Position 1'), ('P2', 'Position 2'), ('P3', 'Position 3')], max_length=50)),
                ('quote', models.CharField(max_length=100)),
                ('social_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.social')),
            ],
        ),
    ]
