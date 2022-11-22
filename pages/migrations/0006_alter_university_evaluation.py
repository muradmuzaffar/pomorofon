# Generated by Django 4.1.3 on 2022-11-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_university_fee_waiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='evaluation',
            field=models.CharField(blank=True, choices=[('Very Difficult; Great', 'Very Difficult; Great'), ('Not Difficult; Great', 'Not Difficult; Great'), ('Mid Difficult; Great', 'Mid Difficult; Great'), ('Easy; Not Good', 'Easy; Not Good'), ('Easy; Okay', 'Easy; Okay'), ('Difficult; Okay', 'Difficult; Okay'), ('Difficult; Great', 'Difficult; Great')], max_length=500, null=True),
        ),
    ]