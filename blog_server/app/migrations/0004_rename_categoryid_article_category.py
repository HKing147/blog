# Generated by Django 4.1 on 2022-08-31 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_authorid_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='categoryId',
            new_name='category',
        ),
    ]
