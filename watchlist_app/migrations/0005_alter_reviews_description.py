# Generated by Django 4.2.7 on 2023-11-21 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]