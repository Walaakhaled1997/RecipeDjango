# Generated by Django 3.1.7 on 2021-04-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsers', '0005_auto_20210422_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='skills',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
