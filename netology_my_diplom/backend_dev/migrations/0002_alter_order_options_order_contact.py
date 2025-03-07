# Generated by Django 5.1.3 on 2025-02-05 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_dev', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-dt',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Список заказов'},
        ),
        migrations.AddField(
            model_name='order',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_dev.contact', verbose_name='Контакт'),
        ),
    ]
