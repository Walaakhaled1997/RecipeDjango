# Generated by Django 3.1.7 on 2021-04-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0003_delete_blogimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogimg', models.ImageField(upload_to='images/blog/')),
            ],
        ),
    ]
