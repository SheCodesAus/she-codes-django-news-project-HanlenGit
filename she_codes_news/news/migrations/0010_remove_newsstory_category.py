# Generated by Django 4.0.1 on 2022-02-19 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_remove_newsstory_categories_newsstory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsstory',
            name='category',
        ),
    ]
