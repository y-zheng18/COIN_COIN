# Generated by Django 3.0 on 2019-12-18 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anno', '0003_auto_20191217_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='step_ids',
            field=models.CharField(default='', max_length=300),
        ),
    ]