# Generated by Django 2.2 on 2020-03-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=300)),
                ('number', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
