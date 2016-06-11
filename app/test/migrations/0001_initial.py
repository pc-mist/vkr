# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 18:30
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.FileField(help_text='^CIPHER^_test_^N^_in.txt', upload_to='tests/inputs/', verbose_name='Файл с входными данными')),
                ('output_etalon', models.FileField(help_text='^CIPHER^_test_^N^_out_etal.txt', upload_to='tests/etalon_outputs/', verbose_name='Файл с эталонными выходными данными')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='TestCaseExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', ckeditor.fields.RichTextField(verbose_name='Пример входных данных')),
                ('ouput', ckeditor.fields.RichTextField(verbose_name='Пример выходных данных')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='TestCasePass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passed', models.BooleanField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Lesson')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.TestCase')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
