# Generated by Django 3.1.4 on 2020-12-25 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages_about_me', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactme',
            old_name='name',
            new_name='author',
        ),
    ]