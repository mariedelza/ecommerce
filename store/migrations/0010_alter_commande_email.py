# Generated by Django 4.0 on 2023-05-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_delete_panier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
