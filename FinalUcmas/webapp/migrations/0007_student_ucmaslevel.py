# Generated by Django 3.1.1 on 2021-05-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20210519_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ucmaslevel',
            field=models.IntegerField(default=1),
        ),
    ]
