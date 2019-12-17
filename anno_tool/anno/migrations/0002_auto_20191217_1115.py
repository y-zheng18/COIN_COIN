# Generated by Django 3.0 on 2019-12-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='steps',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='checkpoint',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, 'NOT ANNOTATED'), (1, 'ANNOTATING'), (2, 'FINISHED')], default=0),
        ),
    ]