# Generated by Django 4.0.7 on 2022-10-12 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bank',
            field=models.CharField(default='Meezan Bank', max_length=25),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp452', max_length=70),
        ),
    ]
