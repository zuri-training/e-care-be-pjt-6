# Generated by Django 3.2.4 on 2021-07-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_hospital_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
