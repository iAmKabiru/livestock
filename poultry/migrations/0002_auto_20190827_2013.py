# Generated by Django 2.2.4 on 2019-08-27 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poultry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='birds',
            name='cost_per_bird',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('birds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poultry.Birds')),
            ],
        ),
    ]