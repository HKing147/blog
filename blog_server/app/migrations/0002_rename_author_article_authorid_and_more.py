# Generated by Django 4.1 on 2022-08-31 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='authorId',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='category',
            new_name='categoryId',
        ),
    ]