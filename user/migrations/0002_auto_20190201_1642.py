# Generated by Django 2.1.5 on 2019-02-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationuser',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='applicationuser',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
