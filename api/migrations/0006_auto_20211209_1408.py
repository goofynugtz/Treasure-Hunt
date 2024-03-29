# Generated by Django 3.2.9 on 2021-12-09 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20211209_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
