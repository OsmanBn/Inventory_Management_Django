# Generated by Django 4.2.7 on 2023-12-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_order_options_alter_product_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='quantity',
            new_name='order_quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
