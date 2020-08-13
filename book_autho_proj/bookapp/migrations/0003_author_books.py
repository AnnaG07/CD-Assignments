# Generated by Django 3.0.6 on 2020-08-04 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_author_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='bookapp.Book'),
        ),
    ]