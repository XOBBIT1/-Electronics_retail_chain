# Generated by Django 4.1.3 on 2022-11-30 13:16

from django.db import migrations, models
import django.db.models.deletion
import esn.validator


class Migration(migrations.Migration):

    dependencies = [
        ("esn", "0003_objectmodel_provider"),
    ]

    operations = [
        migrations.AlterField(
            model_name="objectmodel",
            name="provider",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="esn.objectmodel",
                validators=[esn.validator.validate_even],
            ),
        ),
    ]