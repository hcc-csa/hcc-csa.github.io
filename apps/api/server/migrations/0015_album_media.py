# Generated by Django 5.0.4 on 2024-05-22 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0014_remove_album_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.media'),
        ),
    ]
