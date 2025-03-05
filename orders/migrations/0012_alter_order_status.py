# Generated by Django 5.1.6 on 2025-03-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted'), ('New', 'New')], default='New', max_length=10),
        ),
    ]
