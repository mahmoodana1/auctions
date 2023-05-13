# Generated by Django 4.2 on 2023-05-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_remove_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='listing_category', to='auctions.categories'),
        ),
    ]
