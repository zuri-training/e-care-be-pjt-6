# Generated by Django 3.2.4 on 2021-07-10 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_patient_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
