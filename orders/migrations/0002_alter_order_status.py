# Generated by Django 5.1.6 on 2025-02-19 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('New', 'New'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
    ]
