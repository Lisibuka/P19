# Generated by Django 4.1.1 on 2022-09-14 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categories',
        ),
    ]
