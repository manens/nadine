# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-14 18:35


from django.db import migrations, models
import nadine.models.organization


class Migration(migrations.Migration):

    dependencies = [
        ('nadine', '0020_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='locked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=nadine.models.organization.org_photo_path),
        ),
        migrations.AddField(
            model_name='organizationmember',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organizationmember',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='organizationnote',
            name='private',
            field=models.BooleanField(default=True),
        ),
    ]
