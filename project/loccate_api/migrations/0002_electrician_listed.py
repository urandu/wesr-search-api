# Generated by Django 2.2.10 on 2020-05-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loccate_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='electrician',
            name='listed',
            field=models.BooleanField(default=False),
        ),
    ]
