# Generated by Django 5.0.6 on 2024-09-01 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_paymentrequest_pr_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrequest',
            name='is_accept',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='paymentrequest',
            name='payment_method',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='paymentrequest',
            name='tr_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
