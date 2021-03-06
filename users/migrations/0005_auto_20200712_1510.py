# Generated by Django 3.0.7 on 2020-07-29 14:50

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
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120, null=True)),
                ('lastname', models.CharField(max_length=120, null=True)),
                ('address', models.CharField(max_length=120, null=True)),
                ('address2', models.CharField(max_length=120, null=True)),
                ('address3', models.CharField(max_length=120, null=True)),
                ('city', models.CharField(max_length=120, null=True)),
                ('state', models.CharField(max_length=120, null=True)),
                ('country', models.CharField(max_length=120, null=True)),
                ('zipcode', models.CharField(max_length=120, null=True)),
                ('phone', models.CharField(max_length=120, null=True)),
                ('shipping', models.BooleanField(max_length=120, null=True)),
                ('default', models.BooleanField(default=False)),
                ('billing', models.BooleanField(default=False)),
                ('time_stamp', models.DateTimeField(max_length=120, null=True)),
                ('updated', models.DateTimeField(max_length=120, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-time_stamp'],
            },
        ),
        migrations.CreateModel(
            name='UserStripe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=127)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDefaultAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_address_billing)default+', to='users.UserAddress')),
                ('shipping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_address_shipping_default+', to='users.UserAddress')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120, null=True)),
                ('lastname', models.CharField(max_length=120, null=True)),
                ('address', models.CharField(max_length=120, null=True)),
                ('address2', models.CharField(max_length=120, null=True)),
                ('address3', models.CharField(max_length=120, null=True)),
                ('city', models.CharField(max_length=120, null=True)),
                ('state', models.CharField(max_length=120, null=True)),
                ('country', models.CharField(max_length=120, null=True)),
                ('zipcode', models.CharField(max_length=120, null=True)),
                ('phone', models.CharField(max_length=120, null=True)),
                ('shipping', models.BooleanField(max_length=120, null=True)),
                ('time_stamp', models.DateTimeField(max_length=120, null=True)),
                ('updated', models.DateTimeField(max_length=120, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-time_stamp'],
            },
        ),
    ]