# Generated by Django 3.0.6 on 2020-06-21 02:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200621_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10)),
                ('date', models.DateField(default=datetime.date.today)),
                ('query', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('0', 'IN PROGRESS'), ('1', 'ACCEPTED'), ('2', 'DECLINED')], default='0', max_length=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myapp_query_stud', to='myapp.Student')),
            ],
        ),
    ]
