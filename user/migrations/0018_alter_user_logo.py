# Generated by Django 4.2.5 on 2023-11-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_user_logo_alter_user_municipality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='logo',
            field=models.ImageField(default='user_logo/img.png', null=True, upload_to='user_logo/'),
        ),
    ]
