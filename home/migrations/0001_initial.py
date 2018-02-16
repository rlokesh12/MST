# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-16 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badminton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men', models.IntegerField(blank=True, null=True)),
                ('women', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BasketBall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men', models.IntegerField(blank=True, null=True)),
                ('women', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cricket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Football',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weightLifting', models.IntegerField(blank=True, null=True)),
                ('powerLifting', models.IntegerField(blank=True, null=True)),
                ('bestPhysique', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kabaddi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('women', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('mobile', models.CharField(default='', max_length=11, verbose_name='Mobile No.')),
                ('email_id', models.CharField(max_length=200, verbose_name='Email-id')),
                ('bad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Badminton')),
                ('bas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.BasketBall')),
                ('che', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Chess')),
                ('cri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Cricket')),
                ('foo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Football')),
                ('gym', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Gym')),
                ('kab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Kabaddi')),
            ],
        ),
        migrations.CreateModel(
            name='TableTennis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men', models.IntegerField(blank=True, null=True)),
                ('women', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tennis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men', models.IntegerField(blank=True, null=True)),
                ('women', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volleyball',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men', models.IntegerField(blank=True, null=True)),
                ('women', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='tab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.TableTennis'),
        ),
        migrations.AddField(
            model_name='member',
            name='ten',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Tennis'),
        ),
        migrations.AddField(
            model_name='member',
            name='vol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Volleyball'),
        ),
    ]