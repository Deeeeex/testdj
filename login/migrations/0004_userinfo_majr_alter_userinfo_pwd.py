# Generated by Django 4.0.1 on 2022-01-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_userinfo_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='majr',
            field=models.CharField(default='zhuanye', max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pwd',
            field=models.CharField(max_length=32),
        ),
    ]
