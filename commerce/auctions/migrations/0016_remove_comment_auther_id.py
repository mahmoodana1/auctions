# Generated by Django 4.2 on 2023-05-13 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_comment_auther_name_comment_listing_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='auther_id',
        ),
    ]
