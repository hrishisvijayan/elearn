# Generated by Django 4.0.5 on 2022-06-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': '3. Course '},
        ),
        migrations.AlterModelOptions(
            name='coursecategory',
            options={'verbose_name_plural': '2. Course Categories'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': '4. Student'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': '1. Teacher'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='qualification',
            field=models.CharField(max_length=100),
        ),
    ]
