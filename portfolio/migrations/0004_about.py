# Generated by Django 3.0.8 on 2020-08-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(blank=True, max_length=50, null=True)),
                ('s_Intro', models.CharField(blank=True, max_length=150, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('degree', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('freelance', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
