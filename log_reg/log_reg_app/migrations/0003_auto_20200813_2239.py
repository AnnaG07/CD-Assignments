# Generated by Django 3.0.6 on 2020-08-14 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0002_auto_20200812_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=60),
        ),
    ]
