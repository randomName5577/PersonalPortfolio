# Generated by Django 3.1.4 on 2020-12-29 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FilePathField(default='ok', path='/home/homepc/PycharmProjects/djangoProject/blog/static/images'),
            preserve_default=False,
        ),
    ]
