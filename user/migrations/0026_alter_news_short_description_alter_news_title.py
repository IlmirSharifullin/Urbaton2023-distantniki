# Generated by Django 4.2.5 on 2023-11-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_news_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short_description',
            field=models.TextField(max_length=210),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
