# Generated by Django 3.1.2 on 2020-11-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emitr', '0007_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='notified',
            field=models.IntegerField(default=0),
        ),
    ]