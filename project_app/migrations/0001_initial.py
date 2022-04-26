# Generated by Django 4.0.4 on 2022-04-26 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=11)),
                ('role', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SectionModel',
            fields=[
                ('section_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('grader', models.BooleanField(default=False)),
                ('assigned_ta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project_app.usermodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.coursemodel')),
            ],
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='assigned_instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instuctor', to='project_app.usermodel'),
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='assigned_tas',
            field=models.ManyToManyField(to='project_app.usermodel'),
        ),
    ]
