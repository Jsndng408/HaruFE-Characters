# Generated by Django 3.1.4 on 2020-12-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0015_auto_20201217_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='epithet',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='other',
            field=models.TextField(blank=True, default=''),
        ),
    ]
