# Generated by Django 3.1.5 on 2021-01-24 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('c_integration_app', '0006_auto_20210124_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ci_deploy',
            name='env1',
        ),
    ]