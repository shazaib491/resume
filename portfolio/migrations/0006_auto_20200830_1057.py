# Generated by Django 3.0.8 on 2020-08-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_about_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='introduction',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
