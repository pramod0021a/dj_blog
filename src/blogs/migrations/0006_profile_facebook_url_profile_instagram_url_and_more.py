# Generated by Django 4.1.1 on 2022-09-21 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0005_alter_post_header_image_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="facebook_url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="instagram_url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="images/profile/"),
        ),
        migrations.AddField(
            model_name="profile",
            name="twitter_url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="website_url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="youtube_url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
