# Generated by Django 4.1.2 on 2022-11-14 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0005_alter_employee_accnum_alter_employee_bank_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitment',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrms.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp25764', max_length=70),
        ),
        migrations.AlterField(
            model_name='employee',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('spanish', 'SPANISH'), ('chinese', 'CHINESE'), ('french', 'FRENCH')], default='english', max_length=10),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='phone',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='position',
            field=models.CharField(max_length=25),
        ),
    ]
