# Generated by Django 3.0.5 on 2020-05-10 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_host', models.CharField(max_length=200, verbose_name='Host')),
                ('set_value', models.CharField(max_length=200, verbose_name='System Settings')),
            ],
            options={
                'verbose_name': 'System Settings',
                'verbose_name_plural': 'System Settings',
            },
        ),
    ]