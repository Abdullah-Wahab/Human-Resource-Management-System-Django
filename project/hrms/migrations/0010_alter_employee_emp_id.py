# Generated by Django 4.1.2 on 2022-11-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0009_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp70772', max_length=70),
        ),
    ]
