# Generated by Django 3.0.5 on 2020-07-19 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200719_0621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fratepost',
            name='count',
        ),
        migrations.AddField(
            model_name='fratepost',
            name='rateCount',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
