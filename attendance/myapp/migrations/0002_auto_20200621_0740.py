# Generated by Django 3.0.6 on 2020-06-21 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='prof',
            new_name='taught_by',
        ),
    ]
