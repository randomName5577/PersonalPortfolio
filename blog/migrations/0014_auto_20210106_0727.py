# Generated by Django 3.1.4 on 2021-01-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='abs_image',
            field=models.FilePathField(path='/home/homepc/PycharmProjects/djangoProject/blog/images'),
        ),
    ]
