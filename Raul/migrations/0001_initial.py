# Generated by Django 3.0.6 on 2020-07-09 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.CharField(choices=[('Plates', 'Plates'), ('Pot', 'Pot'), ('Flowers', 'Flowers'), ('Table', 'Table')], default='Plates', max_length=128)),
                ('slug', models.SlugField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='productimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('active', models.BooleanField(default=True)),
                ('thumbnail', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Raul.product')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='size', max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Raul.productimage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Raul.product')),
            ],
        ),
    ]
