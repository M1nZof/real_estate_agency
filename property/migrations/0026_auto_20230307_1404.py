# Generated by Django 2.2.24 on 2023-03-07 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0025_auto_20230307_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grievances', related_query_name='grievance', to='property.Flat'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grievances', related_query_name='grievance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flat',
            field=models.ManyToManyField(db_index=True, related_name='owners', related_query_name='owner', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
