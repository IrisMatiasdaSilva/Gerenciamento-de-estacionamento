# Generated by Django 4.2.3 on 2024-02-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0004_rename_cpf_cliente_cpf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='clinete',
            new_name='cliente',
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='placa',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]