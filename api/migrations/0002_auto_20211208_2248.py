# Generated by Django 3.2.9 on 2021-12-08 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='time',
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount'),
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
