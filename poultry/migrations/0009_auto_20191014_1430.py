# Generated by Django 2.2.4 on 2019-10-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poultry', '0008_auto_20190828_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casualty',
            name='casualty_type',
            field=models.CharField(choices=[('death', 'death'), ('injury', 'injury')], max_length=255),
        ),
    ]
