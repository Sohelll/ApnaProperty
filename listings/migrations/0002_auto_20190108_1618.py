# Generated by Django 2.1.2 on 2019-01-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='length',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='listings',
            name='width',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=5),
        ),
    ]