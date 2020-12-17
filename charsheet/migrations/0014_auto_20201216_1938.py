# Generated by Django 3.1.4 on 2020-12-17 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0013_auto_20201216_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growth',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='growth_set', to='charsheet.charactersheet'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stat_set', to='charsheet.charactersheet'),
        ),
    ]