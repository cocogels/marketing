# Generated by Django 2.2.5 on 2019-10-16 12:52

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommissionSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_type', models.BooleanField(choices=[(1, 'SHS'), (2, 'RegularClass'), (3, 'NightCLass')])),
                ('tuition_percentage', models.SmallIntegerField(null=True)),
                ('misc_fee_status', models.BooleanField(choices=[(True, 'PAID'), (False, 'UNPAID')])),
                ('reg_fee_status', models.BooleanField(choices=[(True, 'PAID'), (False, 'UNPAID')])),
                ('stud_fee_status', models.BooleanField(choices=[(True, 'ENROLLED'), (False, 'DROP')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Commision Details',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='MatriculationCourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Matriculation Course Category',
                'verbose_name_plural': 'Matriculation Course Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MatriculationICLCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Matriculation ICL Category',
                'verbose_name_plural': 'Matriculation ICL Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MatriculationStatusCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Matriculation Status Category',
                'verbose_name_plural': 'Matriculation Status Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SanctionSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_sanction', models.CharField(default='Verbal Warning', max_length=255)),
                ('second_sanction', models.CharField(default='Written Explanation', max_length=255)),
                ('third_sanction', models.CharField(default='Three Days Suspension', max_length=255)),
                ('fourth_sanction', models.CharField(default='Six Days Suspension', max_length=255)),
                ('fifth_sanction', models.CharField(default='Termination', max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
            ],
            options={
                'verbose_name_plural': 'Sanction Details',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='SchoolYearModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.DateField(unique=True)),
                ('end_year', models.DateField(unique=True)),
                ('active_year', models.BooleanField(default=False, help_text='This is Current School Year. There Can Only be one.')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
            ],
            options={
                'verbose_name_plural': 'School Year',
                'ordering': ['-date_created'],
            },
            managers=[
                ('school_year', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TargetSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corporate', models.BigIntegerField(null=True)),
                ('retail', models.BigIntegerField(null=True)),
                ('owwa', models.BigIntegerField(null=True)),
                ('seniorhigh', models.BigIntegerField(null=True)),
                ('higher_ed', models.BigIntegerField(null=True)),
                ('active', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('school_year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='centermanager.SchoolYearModel')),
            ],
            options={
                'verbose_name_plural': 'Target Sheet',
                'ordering': ['-date_created', '-date_updated'],
            },
        ),
        migrations.CreateModel(
            name='Matriculation',
            fields=[
                ('payment_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('cash_amount_per_unit', models.BigIntegerField(null=True)),
                ('cash_miscellaneous_fee', models.BigIntegerField(null=True)),
                ('cash_lab_fee', models.BigIntegerField(null=True)),
                ('cash_registration_fee', models.BigIntegerField(null=True)),
                ('ins_amount_unit', models.BigIntegerField(null=True)),
                ('ins_miscellaneous_fee', models.BigIntegerField(null=True)),
                ('ins_lab_fee', models.BigIntegerField(null=True)),
                ('ins_registration_fee', models.BigIntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centermanager.MatriculationCourseCategory')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centermanager.MatriculationStatusCategory')),
            ],
            options={
                'verbose_name_plural': 'Payment Details',
                'ordering': ['-date_created'],
            },
        ),
    ]
