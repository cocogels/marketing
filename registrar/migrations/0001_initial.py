<<<<<<< HEAD
# Generated by Django 2.2.1 on 2019-10-17 17:34
=======
# Generated by Django 2.2.5 on 2019-10-16 12:52
>>>>>>> 180452339520ca24726b23483e4e66d43307c895

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableCourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Course Category',
                'verbose_name_plural': 'Course Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RequirementsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Requirements Category',
                'verbose_name_plural': 'Requirements Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RequirementsModel',
            fields=[
                ('req_id', models.AutoField(primary_key=True, serialize=False)),
                ('requirements_name', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date Update')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registrar.RequirementsCategory')),
            ],
            options={
                'verbose_name_plural': 'Requirements',
            },
        ),
        migrations.CreateModel(
            name='AvailableCourseModel',
            fields=[
                ('ac_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255, null=True)),
                ('number_unit', models.SmallIntegerField(null=True)),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date Updated')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registrar.AvailableCourseCategory')),
            ],
            options={
                'verbose_name_plural': 'Available Course',
            },
        ),
    ]
