# Generated by Django 3.1.4 on 2021-01-04 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210104_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.ManyToManyField(related_name='categories', to='projects.Technology'),
        ),
    ]
