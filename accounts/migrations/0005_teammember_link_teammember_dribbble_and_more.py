# Generated by Django 5.0.6 on 2024-09-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_teammember_behance_teammember_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='Link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='dribbble',
            field=models.URLField(blank=True, null=True, verbose_name='Dribbble'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='tiwtter',
            field=models.URLField(blank=True, null=True, verbose_name='Tiwtter'),
        ),
    ]