# Generated by Django 3.0.5 on 2020-05-08 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['c_time'], 'verbose_name': 'Users', 'verbose_name_plural': 'Users'},
        ),
    ]
