# Generated by Django 3.0.6 on 2020-05-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
