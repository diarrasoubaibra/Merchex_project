# Generated by Django 4.1.7 on 2023-04-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='description',
        ),
        migrations.RemoveField(
            model_name='band',
            name='sold',
        ),
        migrations.RemoveField(
            model_name='band',
            name='type',
        ),
        migrations.RemoveField(
            model_name='band',
            name='year',
        ),
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')], max_length=5),
        ),
    ]
