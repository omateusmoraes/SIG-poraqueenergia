# Generated by Django 5.0.6 on 2024-07-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0005_agendamento_cliente_servico_delete_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='cliente',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='servico',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Servico',
        ),
    ]
