# Generated by Django 4.2 on 2023-05-10 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_listing_category_listing_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='category_id',
            new_name='category',
        ),
    ]