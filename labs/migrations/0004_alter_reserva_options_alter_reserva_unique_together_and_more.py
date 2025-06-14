# Generated by Django 5.1.7 on 2025-05-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0003_remove_laboratorio_recursos_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserva',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='reserva',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('aprovado', 'Aprovado'), ('rejeitado', 'Rejeitado'), ('cancelado', 'Cancelado')], default='pendente', max_length=10),
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='motivo',
        ),
    ]
