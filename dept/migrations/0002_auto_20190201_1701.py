# Generated by Django 2.1.5 on 2019-02-01 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dept', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplexDept',
            fields=[
                ('dept_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dept.Dept')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complexdept_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=('dept.dept',),
        ),
        migrations.CreateModel(
            name='SimpleDept',
            fields=[
                ('dept_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dept.Dept')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simpledept_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=('dept.dept',),
        ),
        migrations.RemoveField(
            model_name='onetomanydept',
            name='dept_ptr',
        ),
        migrations.RemoveField(
            model_name='onetomanydept',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='onetomanydept',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='onetoonedept',
            name='dept_ptr',
        ),
        migrations.RemoveField(
            model_name='onetoonedept',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='onetoonedept',
            name='sender',
        ),
        migrations.DeleteModel(
            name='OneToManyDept',
        ),
        migrations.DeleteModel(
            name='OneToOneDept',
        ),
    ]