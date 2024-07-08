# Generated by Django 5.0.6 on 2024-07-08 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolutionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(allow_unicode=True, verbose_name='Slug')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='solutions.solutioncategory', verbose_name='Parent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
