# Generated by Django 5.1.1 on 2024-10-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_ad_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_file',
            field=models.FileField(null=True, upload_to='movies/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_image',
            field=models.ImageField(null=True, upload_to='posters/'),
        ),
    ]
