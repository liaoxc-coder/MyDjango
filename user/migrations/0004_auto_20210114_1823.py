# Generated by Django 3.1.4 on 2021-01-14 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_aclass'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aclass',
            options={'ordering': ['cID'], 'verbose_name': '班级', 'verbose_name_plural': '班级管理'},
        ),
    ]
