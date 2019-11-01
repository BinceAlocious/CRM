# Generated by Django 2.2.5 on 2019-11-01 12:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
import timetable.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class_Name', models.CharField(max_length=256, unique=True)),
                ('No_of_Students', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ToApproveTB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Time', models.TimeField()),
                ('End_Time', models.TimeField()),
                ('Date', models.DateField()),
                ('Class_Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.ClassRoom')),
                ('Select_Batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Batch')),
                ('Select_Trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Trainer')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Time', models.TimeField(default=datetime.datetime.now)),
                ('End_Time', models.TimeField()),
                ('Date', models.DateField(default=timetable.models.next_day)),
                ('Class_Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.ClassRoom')),
                ('Select_Batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Batch')),
                ('Select_Trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Trainer')),
            ],
        ),
    ]
