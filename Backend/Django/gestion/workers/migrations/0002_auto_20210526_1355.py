# Generated by Django 3.2.3 on 2021-05-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='worker',
            name='status',
            field=models.CharField(max_length=10),
        ),
    ]