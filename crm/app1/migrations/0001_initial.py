# Generated by Django 2.2.5 on 2019-11-01 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Time', models.TimeField()),
                ('End_Time', models.TimeField()),
                ('Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch_Code', models.CharField(max_length=150, unique=True)),
                ('Active_Status', models.IntegerField(default=1)),
                ('Date', models.DateField()),
                ('Fees', models.CharField(max_length=190)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HrUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Phone_No', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Verify_Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250, unique=True)),
                ('Phone_No', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Verify_Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Qualification', models.CharField(max_length=250)),
                ('Address', models.TextField()),
                ('Phone_No', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Verify_Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=150)),
                ('Payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Payment')),
                ('Select_Batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Batch')),
                ('Select_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Course')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='Select_Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Course'),
        ),
    ]
