# Generated by Django 3.1.1 on 2021-05-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_student_ucmaslevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='FatherEmail',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='MotherEmail',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='StudentEmail',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='StudentFirstName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='StudentLastName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='StudentMiddleName',
            field=models.CharField(max_length=50),
        ),
    ]
