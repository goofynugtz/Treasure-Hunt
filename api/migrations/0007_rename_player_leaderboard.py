# Generated by Django 3.2.9 on 2021-12-09 09:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialaccount', '0003_extra_data_default_dict'),
        ('api', '0006_auto_20211209_1408'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Player',
            new_name='Leaderboard',
        ),
    ]