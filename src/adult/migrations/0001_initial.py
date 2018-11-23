# Generated by Django 2.1.3 on 2018-11-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adult',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('adult', models.CharField(max_length=256)),
                ('workclass', models.CharField(max_length=256)),
                ('fnlwgt', models.CharField(max_length=256)),
                ('education', models.CharField(max_length=256)),
                ('Education_num', models.CharField(max_length=256)),
                ('Marital_status', models.CharField(max_length=256)),
                ('occupation', models.CharField(max_length=256)),
                ('relationship', models.CharField(max_length=256)),
                ('race', models.CharField(max_length=256)),
                ('sex', models.CharField(max_length=256)),
                ('Capital_gain', models.CharField(max_length=256)),
                ('Capital_loss', models.CharField(max_length=256)),
                ('Hours_per_week', models.CharField(max_length=256)),
                ('Native_country', models.CharField(max_length=256)),
                ('salary', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'adult',
                'managed': False,
            },
        ),
    ]
