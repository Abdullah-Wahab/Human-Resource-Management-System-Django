# Generated by Django 4.1.2 on 2022-11-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0003_alter_employee_emp_id_alter_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp948', max_length=70),
        ),
    ]