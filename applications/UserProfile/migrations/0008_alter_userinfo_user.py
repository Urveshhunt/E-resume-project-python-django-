# Generated by Django 4.0 on 2022-03-29 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('UserProfile', '0007_remove_userinfo_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserInfoProfile', to='auth.user'),
        ),
    ]
