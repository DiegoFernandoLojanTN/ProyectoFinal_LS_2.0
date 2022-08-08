# Generated by Django 4.1 on 2022-08-08 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('artista', models.CharField(max_length=200)),
                ('descripcion', models.CharField(default=None, max_length=500)),
                ('fecha', models.CharField(max_length=50, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
                ('lugar', models.CharField(max_length=200, null=True)),
                ('image_url', models.CharField(default=False, max_length=2083)),
                ('ver_instragram', models.CharField(blank=True, max_length=2083)),
                ('evento_valido', models.BooleanField(default=False)),
                ('codigoqr', models.CharField(default=False, max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eventos.evento')),
            ],
        ),
    ]