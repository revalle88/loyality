# Generated by Django 2.0.5 on 2018-05-29 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='card',
            field=models.CharField(default='default0000', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='summ',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]