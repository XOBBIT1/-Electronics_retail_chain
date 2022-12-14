# Generated by Django 4.1.3 on 2022-11-29 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "__first__"),
        ("employees", "0001_initial"),
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ObjectModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=20, null=True
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("FACTORY", "Factory"),
                            ("DISTRIBUTOR", "Distributor"),
                            ("LRC", "Large_retail_chain"),
                            ("DECEMBER", "December"),
                            ("IE", "Individual_entrepreneur"),
                        ],
                        default="FACTORY",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "contacts",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contacts",
                        to="contacts.contacts",
                    ),
                ),
                (
                    "employees",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="employees",
                        to="employees.employees",
                    ),
                ),
                (
                    "product",
                    models.ManyToManyField(
                        null=True, related_name="product", to="products.product"
                    ),
                ),
            ],
        ),
    ]
