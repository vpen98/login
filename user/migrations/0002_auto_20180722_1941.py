# Generated by Django 2.0.5 on 2018-07-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='register_time',
            field=models.DateTimeField(),
        ),
    ]
