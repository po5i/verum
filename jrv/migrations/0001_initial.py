# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-08 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import jrv.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=200)),
                ('parroquia', models.CharField(blank=True, max_length=200, null=True)),
                ('circunscripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('canton', models.CharField(max_length=200)),
                ('junta', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('lasso', models.IntegerField()),
                ('moreno', models.IntegerField()),
                ('blancos', models.IntegerField()),
                ('nulos', models.IntegerField()),
                ('zona', models.CharField(blank=True, max_length=200, null=True)),
                ('foto', models.ImageField(upload_to=jrv.models.get_image_path)),
                ('autor', models.CharField(blank=True, max_length=200, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('useragent', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('flagged', models.BooleanField(default=False)),
                ('verified1', models.BooleanField(default=False)),
                ('verified2', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
