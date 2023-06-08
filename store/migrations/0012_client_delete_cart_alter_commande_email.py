# Generated by Django 4.0 on 2023-05-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.IntegerField(unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.AlterField(
            model_name='commande',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]