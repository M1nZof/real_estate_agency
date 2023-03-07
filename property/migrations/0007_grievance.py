# Generated by Django 2.2.24 on 2023-03-03 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_auto_20230303_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats_grievances', related_query_name='flats_grievance', to='property.Flat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_grievances', related_query_name='user_grievance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]