# Generated by Django 4.0.5 on 2022-06-11 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_course_options_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='qualification',
        ),
    ]
