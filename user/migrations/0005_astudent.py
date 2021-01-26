# Generated by Django 3.1.4 on 2021-01-14 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210114_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='AStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sID', models.CharField(max_length=11, unique=True, verbose_name='学号')),
                ('sname', models.CharField(max_length=128, verbose_name='姓名')),
                ('stel', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('sage', models.CharField(max_length=3, verbose_name='年龄')),
                ('ssex', models.CharField(max_length=1, verbose_name='性别')),
                ('smajor', models.CharField(max_length=128, verbose_name='专业')),
                ('aclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu', to='user.aclass')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生管理s',
                'ordering': ['sID'],
            },
        ),
    ]