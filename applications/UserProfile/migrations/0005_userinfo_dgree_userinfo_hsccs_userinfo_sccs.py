# Generated by Django 4.0 on 2022-03-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0004_remove_userinfo_skill_userinfo_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='dgree',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='hsccs',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='sccs',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
