# Generated by Django 3.0.5 on 2020-05-08 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_auto_20200508_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='apitest',
            name='ApiStep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apitest.ApiStep'),
        ),
    ]
