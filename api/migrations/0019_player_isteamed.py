# Generated by Django 3.2.9 on 2021-12-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20211212_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='isTeamed',
            field=models.BooleanField(default=False),
        ),
    ]
