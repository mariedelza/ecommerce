# Generated by Django 4.0 on 2023-05-24 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_panier_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Panier',
        ),
    ]