# Generated by Django 5.1.6 on 2025-02-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='color',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('New', 'New'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=10),
        ),
    ]
