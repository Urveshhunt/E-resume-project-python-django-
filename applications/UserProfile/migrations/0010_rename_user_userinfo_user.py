# Generated by Django 4.0 on 2022-04-01 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0009_alter_userinfo_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='User',
            new_name='user',
        ),
    ]