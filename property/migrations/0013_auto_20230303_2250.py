# Generated by Django 2.2.24 on 2023-03-03 19:50
import phonenumbers
from django.db import migrations


def add_default_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        parsed_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_phone):
            flat.owner_pure_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
        else:
            flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20230303_2246'),
    ]

    operations = [
        migrations.RunPython(add_default_numbers)
    ]
