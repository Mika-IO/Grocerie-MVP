# Generated by Django 3.2.3 on 2021-06-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitanda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='pendente', max_length=50, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='adress_district',
            field=models.CharField(max_length=250, null=True, verbose_name='endereço de entrega bairro'),
        ),
    ]