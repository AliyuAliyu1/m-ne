# Generated by Django 3.2.13 on 2022-04-12 08:31

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0051_populate_currency_to_checkout_line"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkoutline",
            name="currency",
            field=models.CharField(max_length=3),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="tax_rate",
            field=models.DecimalField(
                decimal_places=2, default=Decimal("0.0"), max_digits=5
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="total_price_gross_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="total_price_net_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="total_price_with_discounts_gross_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="total_price_with_discounts_net_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="undiscounted_total_price_gross_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="undiscounted_total_price_net_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="undiscounted_unit_price_gross_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="undiscounted_unit_price_net_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="unit_price_gross_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="unit_price_net_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="unit_price_with_discounts_gross_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="unit_price_with_discounts_net_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=12
            ),
        ),
    ]
