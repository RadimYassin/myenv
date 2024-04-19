# Generated by Django 5.0.4 on 2024-04-10 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destination_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.DurationField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destination_app.destination')),
            ],
        ),
    ]
