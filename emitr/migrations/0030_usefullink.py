# Generated by Django 3.1.2 on 2021-01-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emitr', '0029_latestupdates_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsefulLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('link', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
