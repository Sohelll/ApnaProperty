# Generated by Django 2.1.2 on 2019-01-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190108_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='length',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='listings',
            name='width',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
    ]
