# Generated by Django 4.0 on 2022-04-01 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0010_rename_user_userinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='college_document',
            field=models.ImageField(default=1, upload_to='image/userprofil/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='hschool_document',
            field=models.ImageField(default=1, upload_to='image/userprofil/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='sccs_document',
            field=models.ImageField(default=1, upload_to='image/userprofil/'),
            preserve_default=False,
        ),
    ]
