# Generated by Django 3.0.6 on 2020-08-17 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log_reg_app', '0003_auto_20200813_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wall_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_content', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='poster_message', to='log_reg_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Wall_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_content', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('message', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comment_message', to='log_reg_app.User')),
                ('poster', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='poster_comment', to='log_reg_app.User')),
            ],
        ),
    ]