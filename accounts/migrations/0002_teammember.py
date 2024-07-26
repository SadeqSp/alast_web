# Generated by Django 5.0.6 on 2024-07-26 10:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(upload_to='mutlimedias/team_members/', verbose_name='Avatar')),
                ('role', models.CharField(blank=True, max_length=150, null=True, verbose_name='Role')),
                ('bio', models.TextField(blank=True, verbose_name='Biography')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
