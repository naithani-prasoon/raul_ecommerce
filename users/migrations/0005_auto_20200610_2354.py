# Generated by Django 3.0.6 on 2020-06-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_merge_20200609_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='address2',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='address3',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='billing',
            field=models.BooleanField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='shipping',
            field=models.BooleanField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='state',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='time_stamp',
            field=models.DateTimeField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='updated',
            field=models.DateTimeField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='zipcode',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
