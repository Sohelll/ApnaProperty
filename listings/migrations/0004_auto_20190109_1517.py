# Generated by Django 2.1.2 on 2019-01-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20190108_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='length',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listings',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]