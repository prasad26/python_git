# Generated by Django 2.0.3 on 2018-03-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.CharField(max_length=200)),
            ],
        ),
    ]
