# Generated by Django 5.0 on 2024-03-13 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevicesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('device_type', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.companymodel')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('joining_time', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.companymodel')),
            ],
        ),
        migrations.CreateModel(
            name='DevicesReturnedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('returned_time', models.DateTimeField()),
                ('device_condition', models.CharField(max_length=100)),
                ('isConditionSatisfy', models.BooleanField()),
                ('divice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.devicesmodel')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employeemodel')),
            ],
        ),
        migrations.CreateModel(
            name='DevicesAssignModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_time', models.DateTimeField()),
                ('returned_deadeline', models.DateTimeField()),
                ('device_condition', models.CharField(max_length=100)),
                ('divice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.devicesmodel')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employeemodel')),
            ],
        ),
    ]
