# Generated by Django 3.2.9 on 2021-12-09 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20211209_2321'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]