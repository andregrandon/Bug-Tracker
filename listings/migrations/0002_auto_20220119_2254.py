# Generated by Django 3.1.2 on 2022-01-19 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='bug_image',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
