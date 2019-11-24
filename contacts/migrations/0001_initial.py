<<<<<<< HEAD
# Generated by Django 2.2.1 on 2019-10-17 17:34
=======
# Generated by Django 2.2.5 on 2019-10-16 12:52
>>>>>>> 180452339520ca24726b23483e4e66d43307c895

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SHS_ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('tel_area', models.CharField(blank=True, default='02', help_text='Area Code For Metro Manila', max_length=2, null=True, validators=[django.core.validators.RegexValidator(message='Area Code Must Contains Two Number', regex='\\d{2}')])),
                ('tel_num_digits', models.CharField(blank=True, max_length=3, null=True, validators=[django.core.validators.RegexValidator(message='invalid input this field must contain atleast 3 numbers', regex='\\d{3}')])),
                ('tel_num', models.CharField(blank=True, max_length=4, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='invalid input this field must contain atleast 4 numbers', regex='\\d{4}$')])),
                ('phone_number', models.CharField(blank=True, default='+63', max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone Number must entered in the format:'+123456789'.Up to 12 digits allowed.", regex='^\\+?1?\\d{9,12}$')])),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('person', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date Updated')),
                ('assigned_to', models.ManyToManyField(related_name='shs_contact_assigned_user', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shs_contact_created_by', to=settings.AUTH_USER_MODEL)),
                ('org_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.SHS_ContactCategoryModel')),
            ],
            options={
                'verbose_name': 'SHS Contact Detail',
                'verbose_name_plural': 'SHSContact Details',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='IHE_ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('tel_area', models.CharField(blank=True, default='02', help_text='Area Code For Metro Manila', max_length=2, null=True, validators=[django.core.validators.RegexValidator(message='Area Code Must Contains Two Number', regex='\\d{2}')])),
                ('tel_num_digits', models.CharField(blank=True, max_length=3, null=True, validators=[django.core.validators.RegexValidator(message='invalid input this field must contain atleast 3 numbers', regex='\\d{3}')])),
                ('tel_num', models.CharField(blank=True, max_length=4, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='invalid input this field must contain atleast 4 numbers', regex='\\d{4}$')])),
                ('phone_number', models.CharField(blank=True, default='+63', max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone Number must entered in the format:'+123456789'.Up to 12 digits allowed.", regex='^\\+?1?\\d{9,12}$')])),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('person', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date Updated')),
                ('assigned_to', models.ManyToManyField(related_name='ihe_contact_assigned_user', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ihe_contact_created_by', to=settings.AUTH_USER_MODEL)),
                ('org_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.IHE_ContactCategoryModel')),
            ],
            options={
                'verbose_name': 'IHE Contact Detail',
                'verbose_name_plural': 'IHE Contact Details',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='ICL_ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('tel_area', models.CharField(blank=True, default='02', help_text='Area Code For Metro Manila', max_length=2, null=True, validators=[django.core.validators.RegexValidator(message='Area Code Must Contains Two Number', regex='\\d{2}')])),
                ('tel_num_digits', models.CharField(blank=True, max_length=3, null=True, validators=[django.core.validators.RegexValidator(message='invalid input this field must contain atleast 3 numbers', regex='\\d{3}')])),
                ('tel_num', models.CharField(blank=True, max_length=4, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='invalid input this field must contain atleast 4 numbers', regex='\\d{4}$')])),
                ('phone_number', models.CharField(blank=True, default='+63', max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone Number must entered in the format:'+123456789'.Up to 12 digits allowed.", regex='^\\+?1?\\d{9,12}$')])),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('person', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateField(auto_now=True)),
                ('assigned_to', models.ManyToManyField(related_name='contact_assigned_user', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_created_by', to=settings.AUTH_USER_MODEL)),
                ('org_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.ICL_ContactCategoryModel')),
            ],
            options={
                'verbose_name': 'ICL Contact Detail',
                'verbose_name_plural': 'ICL Contact Details',
                'ordering': ('-date_created',),
            },
        ),
    ]
