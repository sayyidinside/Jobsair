# Generated by Django 3.1.4 on 2020-12-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobsair_id', '0006_auto_20201224_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag_line',
            field=models.CharField(default='Tag line unavailable', max_length=100),
        ),
    ]