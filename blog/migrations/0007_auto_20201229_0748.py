# Generated by Django 3.1.4 on 2020-12-29 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201229_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(path='/home/homepc/PycharmProjects/djangoProject/projects/static/img'),
        ),
    ]
