# Generated by Django 3.2.3 on 2021-06-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_auto_20210607_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='photo',
            field=models.ImageField(default=None, upload_to='', verbose_name='Uploaded image'),
        ),
    ]