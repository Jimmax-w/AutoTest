# Generated by Django 3.0.7 on 2020-06-30 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appcase',
            name='app_case_step',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apptest.AppCaseStep'),
        ),
    ]
