# Generated by Django 3.1.4 on 2021-01-11 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('c_integration_app', '0002_auto_20201231_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ci_envs',
            name='ci_deploy',
        ),
        migrations.AddField(
            model_name='ci_deploy',
            name='envs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='c_integration_app.ci_envs'),
            preserve_default=False,
        ),
    ]
