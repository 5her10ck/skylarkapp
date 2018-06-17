# Generated by Django 2.0.6 on 2018-06-13 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0005_matchdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.RemoveField(
            model_name='matchdate',
            name='match',
        ),
        migrations.DeleteModel(
            name='MatchDate',
        ),
    ]
