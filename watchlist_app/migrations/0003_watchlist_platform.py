# Generated by Django 4.2.7 on 2023-11-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_streamingplatform_watchlist_delete_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ManyToManyField(blank=True, to='watchlist_app.streamingplatform'),
        ),
    ]
