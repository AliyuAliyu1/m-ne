# Generated by Django 3.2.14 on 2022-07-08 10:05

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0055_auto_20220505_0914"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkout",
            name="shipping_tax_rate",
            field=models.DecimalField(
                decimal_places=4, default=Decimal("0.0"), max_digits=5
            ),
        ),
        migrations.AlterField(
            model_name="checkoutline",
            name="tax_rate",
            field=models.DecimalField(
                decimal_places=4, default=Decimal("0.0"), max_digits=5
            ),
        ),
    ]
