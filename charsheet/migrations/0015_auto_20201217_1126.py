# Generated by Django 3.1.4 on 2020-12-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0014_auto_20201216_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='epithet',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='other',
            field=models.TextField(null=True),
        ),
    ]
