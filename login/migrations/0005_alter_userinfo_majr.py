# Generated by Django 4.0.1 on 2022-01-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_userinfo_majr_alter_userinfo_pwd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='majr',
            field=models.CharField(max_length=32),
        ),
    ]
