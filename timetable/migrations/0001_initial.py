# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('day', models.CharField(max_length=64)),
                ('timing', models.CharField(max_length=32)),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Teacher')),
                ('classLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.ClassLevel')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Room')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Subject')),
            ],
        ),
    ]
