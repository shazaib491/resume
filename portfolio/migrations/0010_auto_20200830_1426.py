# Generated by Django 3.0.8 on 2020-08-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('caption', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
