# Generated by Django 3.0.7 on 2020-07-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200628_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now_add=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('servico', models.CharField(max_length=100, verbose_name='Serviço')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descricao')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Computador'), ('lni-leaf', 'Folha_Arvores'), ('lni-layers', 'Multiplos_Templates'), ('lni-leaf', 'Contato_Trabaho')], max_length=20, verbose_name='Icone')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
