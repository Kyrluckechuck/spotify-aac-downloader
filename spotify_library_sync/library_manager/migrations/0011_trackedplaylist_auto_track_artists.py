# Generated by Django 5.0.2 on 2024-02-23 22:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library_manager", "0010_artist_added_at_artist_last_synced_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="trackedplaylist",
            name="auto_track_artists",
            field=models.BooleanField(default=False),
        ),
    ]
