# Generated by Django 4.1.3 on 2022-12-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_transactions_organisation_id_transactions_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]