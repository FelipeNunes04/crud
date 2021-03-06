# Generated by Django 2.0.7 on 2018-08-08 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='setor',
            options={'verbose_name_plural': 'Setores'},
        ),
        migrations.AddField(
            model_name='setor',
            name='empresa',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='app.Empresa'),
            preserve_default=False,
        ),
    ]
