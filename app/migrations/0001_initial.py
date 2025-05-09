# Generated by Django 5.2.1 on 2025-05-09 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField(blank=True)),
                ('data_nascimento', models.DateField()),
                ('is_ativo', models.BooleanField(default=True)),
                ('outro_campo', models.BooleanField(default=False)),
            ],
        ),
    ]
