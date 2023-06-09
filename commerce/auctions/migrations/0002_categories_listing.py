# Generated by Django 4.2 on 2023-05-09 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('bid', models.IntegerField()),
                ('image', models.ImageField(upload_to='uploads')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.categories')),
            ],
        ),
    ]
