# Generated by Django 3.2.9 on 2021-11-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_alter_student_joiningdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='JoiningDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
