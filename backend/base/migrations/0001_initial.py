# Generated by Django 4.1.2 on 2022-10-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeModelTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('logradouro', models.TextField(blank=True, null=True, verbose_name='Logradouro')),
                ('numero', models.CharField(blank=True, max_length=128, null=True, verbose_name='Número')),
                ('bairro', models.CharField(blank=True, max_length=255, null=True, verbose_name='Bairro')),
                ('localidade', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cidade')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True, verbose_name='UF')),
                ('inscricao_estadual', models.CharField(blank=True, max_length=55, null=True, verbose_name='Inscrição Estadual')),
                ('inscricao_municipal', models.CharField(blank=True, max_length=55, null=True, verbose_name='Inscrição Municipal')),
                ('codigo_municipio', models.CharField(blank=True, max_length=55, null=True, verbose_name='Código Município')),
                ('complemento', models.TextField(blank=True, null=True, verbose_name='Complemento')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
