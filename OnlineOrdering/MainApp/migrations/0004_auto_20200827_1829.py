# Generated by Django 3.0 on 2020-08-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='order',
            name='postalcode',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
