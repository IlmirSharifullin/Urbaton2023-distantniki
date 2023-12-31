# Generated by Django 4.2.5 on 2023-11-25 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_alter_municipality_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='is_answered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='municipality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.municipality'),
        ),
    ]
