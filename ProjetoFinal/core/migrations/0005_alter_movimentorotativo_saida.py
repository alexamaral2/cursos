# Generated by Django 4.1.4 on 2022-12-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_movimentorotativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentorotativo',
            name='saida',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
