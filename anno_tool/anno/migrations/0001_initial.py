# Generated by Django 3.0 on 2019-12-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=200)),
                ('cut_points', models.CharField(max_length=200)),
                ('state', models.SmallIntegerField(choices=[(0, 'NOT ANNOTATED'), (1, 'ANNOTATING'), (2, 'FINISHED')], default=0)),
                ('checkpoint', models.SmallIntegerField(default=0)),
            ],
        ),
    ]