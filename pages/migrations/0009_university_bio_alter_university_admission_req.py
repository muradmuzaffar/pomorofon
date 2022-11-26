# Generated by Django 4.1.3 on 2022-11-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_rename_public_university_program_rank_region_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='bio',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='admission_req',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]