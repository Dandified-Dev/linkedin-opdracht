# Generated by Django 5.0.6 on 2024-06-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedin_url', '0007_alter_education_end_date_alter_experience_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.CharField(max_length=1000),
        ),
    ]
