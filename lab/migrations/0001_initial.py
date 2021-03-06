# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-16 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=350)),
                ('price', models.FloatField()),
                ('prerequisite', models.CharField(max_length=350)),
                ('estimate_hours', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('full_name', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='clinicaltest',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Lab'),
        ),
    ]
