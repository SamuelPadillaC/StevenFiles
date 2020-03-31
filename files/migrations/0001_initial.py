# Generated by Django 3.0.2 on 2020-03-29 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('age', models.IntegerField()),
                ('country_of_citizenship', models.CharField(max_length=300)),
                ('morningside_ID', models.IntegerField()),
                ('sevis_ID', models.IntegerField()),
                ('profile_picture', models.ImageField(upload_to='<PATH>')),
                ('email', models.EmailField(max_length=254)),
                ('major', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=300)),
                ('student_class', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='<PATH>')),
                ('file_type', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(verbose_name='date published')),
                ('belongs_to_student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='files.Student')),
            ],
        ),
    ]
