# Generated by Django 4.1.3 on 2022-12-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transactions_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='organisation_id',
            field=models.IntegerField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='payment_id',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
