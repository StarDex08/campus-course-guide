# Generated by Django 4.2.5 on 2024-08-18 15:53

import apps_users.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('user_type', models.CharField(blank=True, choices=[('Student', 'Student'), ('Teaching Assistant', 'Teaching Assistant'), ('Lecturer', 'Lecturer')], max_length=255, null=True)),
                ('programme', models.CharField(blank=True, choices=[('Computer Engineering', 'Computer Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Petroleum Engineering', 'Petroleum Engineering'), ('Materials Engineering', 'Materials Engineering'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Marine Engineering', 'Marine Engineering'), ('Biomedical Engineering', 'Biomedical Engineering'), ('Agric Engineering', 'Agric Engineering')], max_length=255, null=True)),
                ('year', models.CharField(blank=True, choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year'), ('5th Year', '5th Year'), ('6th Year', '6th Year'), ('Completed', 'Completed')], max_length=255, null=True)),
                ('college', models.CharField(blank=True, choices=[('Engineering', 'Engineering'), ('Science', 'Science'), ('Humanities', 'Humanities')], max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', apps_users.models.CustomUserManager()),
            ],
        ),
    ]
