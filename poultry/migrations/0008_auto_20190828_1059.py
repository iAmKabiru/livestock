# Generated by Django 2.2.4 on 2019-08-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poultry', '0007_casualty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casualty',
            options={'verbose_name_plural': 'Casualties'},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_type',
            field=models.CharField(choices=[('feed', 'feed'), ('birds', 'birds'), ('medicine', 'medicine'), ('equipement', 'equipement')], max_length=255),
        ),
    ]
