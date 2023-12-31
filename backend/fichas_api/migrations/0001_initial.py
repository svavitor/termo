# Generated by Django 5.0 on 2023-12-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_cnpj', models.BigIntegerField(default=False)),
                ('nome', models.CharField(max_length=255)),
                ('identidade', models.BigIntegerField(default=False)),
                ('profissao', models.CharField(max_length=200)),
                ('naturalidade', models.CharField(max_length=200)),
                ('estado_civil', models.CharField(max_length=255)),
                ('endereco', models.TextField(max_length=500)),
            ],
        ),
    ]
