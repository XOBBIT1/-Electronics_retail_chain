# Generated by Django 3.2.9 on 2022-11-25 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employees', models.CharField(max_length=256)),
                ('contacts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts_dealership', to='contacts.contacts')),
                ('product', models.ManyToManyField(null=True, related_name='product_dealership', to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='LargeRetailChain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employees', models.CharField(max_length=256)),
                ('contacts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts_lrc', to='contacts.contacts')),
                ('product', models.ManyToManyField(null=True, related_name='product_lrc', to='products.Product')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_lrc', to='esn.dealership')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualEntrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employees', models.CharField(max_length=256)),
                ('contacts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts_ie', to='contacts.contacts')),
                ('product', models.ManyToManyField(null=True, related_name='product_ie', to='products.Product')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_ie', to='esn.largeretailchain')),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employees', models.CharField(max_length=256)),
                ('contacts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts_factory', to='contacts.contacts')),
                ('product', models.ManyToManyField(null=True, related_name='product_factory', to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employees', models.CharField(max_length=256)),
                ('contacts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts_distributor', to='contacts.contacts')),
                ('product', models.ManyToManyField(null=True, related_name='product_distributor', to='products.Product')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_distributor', to='esn.factory')),
            ],
        ),
        migrations.AddField(
            model_name='dealership',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_dealership', to='esn.distributor'),
        ),
    ]
