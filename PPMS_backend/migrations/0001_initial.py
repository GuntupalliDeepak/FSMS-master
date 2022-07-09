# Generated by Django 2.2.2 on 2019-11-25 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DieselDensity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('morningObservedHydroDensity', models.IntegerField(default=0)),
                ('morningObservedTemperatureDensity', models.FloatField(default=0)),
                ('morningDensity', models.FloatField(default=0)),
                ('receiptsInvoiceNumber', models.IntegerField(default=0)),
                ('receiptsQuantity', models.IntegerField(default=0)),
                ('receiptsObservedHydroDensity', models.FloatField(default=0)),
                ('receiptsObservedTemperatureDensity', models.FloatField(default=0)),
                ('receiptsDensity', models.FloatField(default=0)),
                ('asPerChallanDensity', models.FloatField(default=0)),
                ('decantationObservedHydroDensity', models.IntegerField(default=0)),
                ('decantationObservedTemperatureDensity', models.FloatField(default=0)),
                ('decantationDensity', models.FloatField(default=0)),
                ('densityDifference', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DieselNozzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('openingReadingForNozzle1', models.FloatField()),
                ('openingReadingForNozzle2', models.FloatField()),
                ('openingReadingForNozzle3', models.FloatField()),
                ('openingReadingForNozzle4', models.FloatField()),
                ('saleForNozzle1', models.FloatField(default=0)),
                ('saleForNozzle2', models.FloatField(default=0)),
                ('saleForNozzle3', models.FloatField(default=0)),
                ('saleForNozzle4', models.FloatField(default=0)),
                ('totalMeterSale', models.FloatField()),
                ('testing', models.IntegerField(default=0)),
                ('rate', models.FloatField()),
                ('totalAmount', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DieselStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('openingStock', models.FloatField(default=0)),
                ('receiptStock', models.FloatField(default=0)),
                ('totalStock', models.FloatField()),
                ('actualSale', models.FloatField(default=0)),
                ('closingStock', models.FloatField()),
                ('productDip', models.FloatField(default=0)),
                ('actualDip', models.FloatField(default=0)),
                ('variations', models.FloatField(default=0)),
                ('waterCm', models.FloatField(default=0)),
                ('waterLtrs', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PetrolDensity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('morningObservedHydroDensity', models.IntegerField(default=0)),
                ('morningObservedTemperatureDensity', models.FloatField(default=0)),
                ('morningDensity', models.FloatField(default=0)),
                ('receiptsInvoiceNumber', models.IntegerField(default=0)),
                ('receiptsQuantity', models.IntegerField(default=0)),
                ('receiptsObservedHydroDensity', models.FloatField(default=0)),
                ('receiptsObservedTemperatureDensity', models.FloatField(default=0)),
                ('receiptsDensity', models.FloatField(default=0)),
                ('asPerChallanDensity', models.FloatField(default=0)),
                ('decantationObservedHydroDensity', models.IntegerField(default=0)),
                ('decantationObservedTemperatureDensity', models.FloatField(default=0)),
                ('decantationDensity', models.FloatField(default=0)),
                ('densityDifference', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PetrolNozzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Should n0t be null')),
                ('openingReadingForNozzle1', models.FloatField()),
                ('openingReadingForNozzle2', models.FloatField()),
                ('openingReadingForNozzle3', models.FloatField()),
                ('openingReadingForNozzle4', models.FloatField()),
                ('saleForNozzle1', models.FloatField(default=0)),
                ('saleForNozzle2', models.FloatField(default=0)),
                ('saleForNozzle3', models.FloatField(default=0)),
                ('saleForNozzle4', models.FloatField(default=0)),
                ('totalMeterSale', models.FloatField()),
                ('testing', models.IntegerField(default=0)),
                ('rate', models.FloatField()),
                ('totalAmount', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PetrolStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('openingStock', models.FloatField(default=0)),
                ('receiptStock', models.FloatField(default=0)),
                ('totalStock', models.FloatField()),
                ('actualSale', models.FloatField(default=0)),
                ('closingStock', models.FloatField()),
                ('productDip', models.FloatField(default=0)),
                ('actualDip', models.FloatField(default=0)),
                ('variations', models.FloatField(default=0)),
                ('waterCm', models.FloatField(default=0)),
                ('waterLtrs', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('invoiceNumber', models.IntegerField(unique_for_date=True)),
                ('petrolQuantity', models.IntegerField(blank=True)),
                ('dieselQuantity', models.IntegerField(blank=True)),
                ('lubricantQuantity', models.IntegerField(blank=True)),
                ('invoiceAmount', models.IntegerField()),
                ('cheque_demand_number', models.IntegerField()),
                ('paymentDate', models.DateField()),
                ('amountPaid', models.IntegerField()),
                ('amountRemainPaid', models.IntegerField()),
                ('shortExcess', models.IntegerField(null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]