# Generated by Django 3.1.2 on 2020-12-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emitr', '0017_auto_20201227_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='status',
            field=models.CharField(default='Due', max_length=10),
        ),
    ]
