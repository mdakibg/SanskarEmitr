# Generated by Django 3.1.2 on 2020-12-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emitr', '0008_query_notified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=999)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]