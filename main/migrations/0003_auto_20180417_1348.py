# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-17 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180404_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefenseTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occurrenceDate', models.DateField(verbose_name='تاریخ')),
                ('startTime', models.TimeField(verbose_name='زمان شروع')),
                ('endTime', models.TimeField(verbose_name='زمان پایان')),
            ],
            options={
                'verbose_name': 'زمان دفاع',
                'verbose_name_plural': 'زمان\u200cهای دفاع',
            },
        ),
        migrations.AlterModelOptions(
            name='defenseplace',
            options={'verbose_name': 'محل دفاع', 'verbose_name_plural': 'محل\u200cهای دفاع'},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'verbose_name': 'نیمسال تحصیلی', 'verbose_name_plural': 'نیمسال\u200cهای تحصیلی'},
        ),
        migrations.AlterField(
            model_name='defenseplace',
            name='buildingName',
            field=models.CharField(max_length=50, verbose_name='نام ساختمان'),
        ),
        migrations.AlterField(
            model_name='defenseplace',
            name='placeName',
            field=models.CharField(max_length=50, verbose_name='نام مستعار اتاق دفاع'),
        ),
        migrations.AlterField(
            model_name='defenseplace',
            name='roomName',
            field=models.CharField(max_length=50, verbose_name='نام یا شماره اتاق'),
        ),
        migrations.AlterField(
            model_name='defenseplace',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Semester', verbose_name='نیمسال تحصیلی'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='beginningYear',
            field=models.IntegerField(verbose_name='سال شروع'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='endingYear',
            field=models.IntegerField(verbose_name='سال پایان'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semesterType',
            field=models.IntegerField(choices=[(1, 'پاییز'), (2, 'بهار'), (3, 'تابستان')], verbose_name='نوع نیمسال'),
        ),
        migrations.AddField(
            model_name='defensetime',
            name='defensePlace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.DefensePlace', verbose_name='محل دفاع'),
        ),
    ]
