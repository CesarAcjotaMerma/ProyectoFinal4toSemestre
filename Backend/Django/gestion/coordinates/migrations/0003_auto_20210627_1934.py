# Generated by Django 3.1.7 on 2021-06-28 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinates', '0002_auto_20210624_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinates',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]