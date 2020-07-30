# Generated by Django 3.0.7 on 2020-07-30 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last4', models.CharField(max_length=120, unique=True)),
                ('exp', models.CharField(max_length=120, unique=True)),
                ('card_id', models.CharField(max_length=120, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='ABC', max_length=120, unique=True)),
                ('status', models.CharField(choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], default='Started', max_length=120)),
                ('sub_total', models.DecimalField(decimal_places=2, default=1000.0, max_digits=1000)),
                ('tax_total', models.DecimalField(decimal_places=2, default=1000.0, max_digits=1000)),
                ('final_total', models.DecimalField(decimal_places=2, default=1000.0, max_digits=1000)),
                ('Tracking_Status', models.CharField(blank=True, choices=[('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Cancelled', 'Cancelled')], default='Processing', max_length=120, null=True)),
                ('Shipping', models.DecimalField(blank=True, decimal_places=2, default=9.0, max_digits=1000, max_length=120, null=True)),
                ('Tracking_Number', models.CharField(blank=True, max_length=120, null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('order_pdf', models.FileField(blank=True, null=True, upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='users.BillingAddress')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='users.UserAddress')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
