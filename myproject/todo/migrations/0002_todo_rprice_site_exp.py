# Generated by Django 4.2.7 on 2024-04-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='RPRICE_SITE_EXP',
            field=models.DecimalField(decimal_places=4, max_digits=15, null=True),
        ),
    ]
