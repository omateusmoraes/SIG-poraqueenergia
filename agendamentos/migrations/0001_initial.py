# Generated by Django 3.1.4 on 2024-06-27 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('servico', models.CharField(max_length=100)),
                ('profissional', models.CharField(max_length=100)),
            ],
        ),
    ]
