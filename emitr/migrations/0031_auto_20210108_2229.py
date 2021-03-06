# Generated by Django 3.1.2 on 2021-01-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emitr', '0030_usefullink'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='LatestUpdates',
        ),
        migrations.RenameField(
            model_name='usefullink',
            old_name='link',
            new_name='url',
        ),
    ]
