# Generated by Django 3.2.9 on 2021-11-04 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20210912_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='JoiningDate',
            field=models.DateTimeField(null=True),
        ),
    ]
