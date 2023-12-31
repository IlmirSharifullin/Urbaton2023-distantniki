# Generated by Django 4.2.5 on 2023-11-25 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_user_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='logo',
            field=models.ImageField(default='user_logo/img.png', upload_to='user_logo/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='municipality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.municipality'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Мужчина'), ('F', 'Женщина')]),
        ),
    ]
