# Generated by Django 4.1.3 on 2022-11-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('qs', models.CharField(blank=True, max_length=50, null=True)),
                ('us', models.CharField(blank=True, max_length=50, null=True)),
                ('public', models.CharField(blank=True, max_length=50, null=True)),
                ('program', models.CharField(blank=True, max_length=100, null=True)),
                ('degree', models.CharField(blank=True, max_length=100, null=True)),
                ('study_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('other_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gre', models.CharField(blank=True, max_length=100, null=True)),
                ('gpa', models.CharField(blank=True, max_length=100, null=True)),
                ('ielts', models.CharField(blank=True, max_length=100, null=True)),
                ('toefl', models.CharField(blank=True, max_length=100, null=True)),
                ('fee', models.CharField(blank=True, max_length=100, null=True)),
                ('fee_waiver', models.CharField(blank=True, max_length=100, null=True)),
                ('tutaion_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('admission_req', models.CharField(blank=True, max_length=300, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('acceptance_rate', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_rate', models.CharField(blank=True, max_length=100, null=True)),
                ('evaluation', models.CharField(blank=True, max_length=500, null=True)),
                ('dedline', models.CharField(blank=True, max_length=500, null=True)),
                ('result', models.CharField(blank=True, max_length=500, null=True)),
                ('link', models.URLField()),
            ],
        ),
    ]
