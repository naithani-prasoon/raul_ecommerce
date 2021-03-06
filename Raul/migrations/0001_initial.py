# Generated by Django 3.0.7 on 2020-08-06 01:39

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
                ('category', models.CharField(choices=[('Plates', 'Plates'), ('Pot', 'Pot'), ('Flowers', 'Flowers'), ('Table', 'Table'), ('Candlelight', 'Candlelight'), ('Decorative Objects', 'Decorative Objects'), ('Urns', 'Urns'), ('Dinnerware', 'Dinnerware'), ('Pitchers', 'Pitchers'), ('Chairs', 'Chairs'), ('End Tables', 'End Tables'), ('Ottoman & Benches', 'Ottoman & Benches'), ('Outdoor Furniture', 'Outdoor Furniture'), ('ArtWork', 'ArtWork'), ('Mirrors', 'Mirrors'), ('All Sale Items', 'All Sale Items'), ('Bowls', 'Bowls'), ('Glassware', 'Glassware'), ('Vases and Cachepots', 'Vases and Cachepots'), ('Votives', 'Votives'), ('Wall Art', 'Wall Art'), ('Rug Collection', 'Rug Collection'), ('Pot Collection', 'Pot Collection'), ('Layout Shop', 'Layout Shop')], max_length=128)),
                ('section', models.CharField(choices=[('Plates', 'Plates'), ('New Arrivals', 'New Arrivals'), ('Decorative Accessories', 'Decorative Accessories'), ('Furniture', 'Furniture'), ('Floral', 'Floral'), ('Tabletop', 'Tabletop'), ('Wall Art', 'Wall Art'), ('Sale', 'Sale'), ('Rug Collection', 'Rug Collection'), ('Pot Collection', 'Pot Collection'), ('Shopping The Layout', 'Shopping The Layout')], max_length=128)),
                ('slug', models.SlugField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('imageFound', models.BooleanField(default=False)),
                ('Overweight', models.BooleanField(default=False)),
                ('SuperOverweight', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='size', max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Raul.product')),
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
            name='FeatuedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Raul.product')),
            ],
        ),
    ]
