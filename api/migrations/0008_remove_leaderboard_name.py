# Generated by Django 3.2.9 on 2021-12-09 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_player_leaderboard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='name',
        ),
    ]
