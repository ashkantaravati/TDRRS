# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 18:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20180417_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=100, verbose_name='نام رشته')),
            ],
            options={
                'verbose_name': 'رشته\u200cی تحصیلی',
                'verbose_name_plural': 'رشته\u200c\u200cهای تحصیلی',
            },
        ),
        migrations.CreateModel(
            name='ReservationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date_time', django_jalali.db.models.jDateTimeField(verbose_name='زمان ثبت درخواست')),
            ],
            options={
                'verbose_name': 'درخواست رزرو',
                'verbose_name_plural': 'درخواست\u200cهای رزرو',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(max_length=12, verbose_name='شماره دانشجویی')),
                ('degree', models.IntegerField(choices=[(1, 'کارشناسی ارشد'), (2, 'دکتری')], verbose_name='مقطع تحصیلی')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Major', verbose_name='رشته\u200cی تحصیلی')),
                ('user_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='حساب کاربری')),
            ],
            options={
                'verbose_name': 'دانشجو',
                'verbose_name_plural': 'دانشجویان',
            },
        ),
        migrations.RenameField(
            model_name='defenseplace',
            old_name='buildingName',
            new_name='building_name',
        ),
        migrations.RenameField(
            model_name='defenseplace',
            old_name='placeName',
            new_name='place_name',
        ),
        migrations.RenameField(
            model_name='defenseplace',
            old_name='roomName',
            new_name='room_name',
        ),
        migrations.RenameField(
            model_name='defensetime',
            old_name='endTime',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='defensetime',
            old_name='startTime',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='semester',
            old_name='beginningYear',
            new_name='beginning_year',
        ),
        migrations.RenameField(
            model_name='semester',
            old_name='endingYear',
            new_name='ending_year',
        ),
        migrations.RenameField(
            model_name='semester',
            old_name='semesterType',
            new_name='semester_type',
        ),
        migrations.RemoveField(
            model_name='defensetime',
            name='occurrenceDate',
        ),
        migrations.AddField(
            model_name='defensetime',
            name='occurrence_date',
            field=django_jalali.db.models.jDateField(default='1397-02-20', verbose_name='تاریخ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='defensetime',
            name='status',
            field=models.IntegerField(choices=[(0, 'اختصاص داده شده'), (1, 'آزاد')], default=1, verbose_name='وضعیت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservationrequest',
            name='requested_defense_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.DefenseTime', verbose_name='زمان درخواستی'),
        ),
        migrations.AddField(
            model_name='reservationrequest',
            name='requesting_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student', verbose_name='دانشجوی درخواست\u200cکننده'),
        ),
    ]
