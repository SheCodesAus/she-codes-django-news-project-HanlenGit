# Generated by Django 4.0.1 on 2022-02-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_alter_newsstory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='category',
            field=models.CharField(choices=[('NEWS', 'News'), ('PROGRAM', 'Program'), ('ANNOUNCEMENTS', 'Announcements'), ('CAREERS', 'Careers')], default='news', max_length=200),
        ),
    ]
