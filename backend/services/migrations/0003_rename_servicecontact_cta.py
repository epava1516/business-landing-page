# Generated by Django 4.2.1 on 2023-05-15 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_servicecontact_servicelist_delete_service_contact_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceContact',
            new_name='Cta',
        ),
    ]