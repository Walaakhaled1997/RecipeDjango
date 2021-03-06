# Generated by Django 3.1.7 on 2021-04-18 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppUsers', '0001_initial'),
        ('AppJob', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('published_at', models.DateTimeField(null=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUsers.users')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentStr', models.TextField()),
                ('startTime', models.DateTimeField()),
                ('blogID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlog.blog')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUsers.users')),
            ],
        ),
        migrations.CreateModel(
            name='blogImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogimg', models.ImageField(upload_to='images/blog/')),
                ('blogID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlog.blog')),
            ],
        ),
        migrations.CreateModel(
            name='tagsBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlog.blog')),
                ('tagID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppJob.tags')),
            ],
            options={
                'unique_together': {('tagID', 'blogID')},
            },
        ),
    ]
