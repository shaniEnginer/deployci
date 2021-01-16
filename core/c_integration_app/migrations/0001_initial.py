# Generated by Django 3.0.7 on 2020-12-31 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ci_deploy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ci_envs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(default='github', max_length=255)),
                ('url_repo', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ci_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('deploy', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='c_integration_app.Ci_deploy')),
            ],
        ),
        migrations.AddField(
            model_name='ci_deploy',
            name='envs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='c_integration_app.Ci_envs'),
        ),
    ]