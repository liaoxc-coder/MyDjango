# Generated by Django 3.1.4 on 2021-01-13 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210113_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='AClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cID', models.CharField(max_length=11, unique=True, verbose_name='班级ID')),
                ('cn', models.CharField(max_length=128, verbose_name='班级名称')),
                ('cETD', models.CharField(max_length=128, verbose_name='学院/系名称')),
                ('cadmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cls', to='user.ccituser')),
            ],
            options={
                'verbose_name': '班级',
                'db_table': 'classes_table',
                'ordering': ['cID'],
            },
        ),
    ]
