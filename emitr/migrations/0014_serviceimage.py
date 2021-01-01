# Generated by Django 3.1.2 on 2020-12-23 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emitr', '0013_service_subservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/service')),
                ('service_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='emitr.service')),
            ],
        ),
    ]