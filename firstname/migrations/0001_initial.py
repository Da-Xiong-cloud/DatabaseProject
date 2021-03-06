# Generated by Django 4.0 on 2022-01-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dynasty',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='朝代名称')),
                ('begin', models.DateField(verbose_name='起始时间')),
                ('end', models.DateField(verbose_name='终止时间')),
            ],
            options={
                'verbose_name': '朝代',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='省份名称')),
            ],
            options={
                'verbose_name': '省份',
            },
        ),
        migrations.CreateModel(
            name='SecondName',
            fields=[
                ('second_name', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='姓氏')),
                ('base_information', models.CharField(max_length=1024, verbose_name='基本信息')),
                ('fam', models.CharField(max_length=1024, verbose_name='历代名人')),
                ('mig', models.CharField(max_length=1024, verbose_name='迁徙传播')),
                ('dis', models.CharField(max_length=1024, verbose_name='人口分布')),
                ('ori', models.CharField(max_length=1024, verbose_name='姓氏起源')),
                ('cul', models.CharField(max_length=1024, verbose_name='姓氏文化')),
                ('father_surename', models.ManyToManyField(related_name='origin', to='firstname.SecondName')),
            ],
            options={
                'verbose_name': '姓氏',
            },
        ),
        migrations.CreateModel(
            name='Famous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FloatField(verbose_name='姓名')),
                ('begin', models.DateField(verbose_name='出生时间')),
                ('end', models.DateField(verbose_name='死亡时间')),
                ('info', models.CharField(max_length=50, verbose_name='简介')),
                ('姓氏', models.ManyToManyField(to='firstname.SecondName')),
                ('省份', models.ManyToManyField(to='firstname.Province')),
            ],
            options={
                'verbose_name': '姓氏名人',
            },
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.FloatField(verbose_name='比例')),
                ('姓氏', models.ManyToManyField(to='firstname.SecondName')),
                ('省份', models.ManyToManyField(to='firstname.Province')),
            ],
            options={
                'verbose_name': '人口分布',
            },
        ),
    ]
