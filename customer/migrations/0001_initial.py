# Generated by Django 3.2.7 on 2022-10-23 06:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('custId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('custFname', models.CharField(max_length=100)),
                ('custLname', models.CharField(max_length=100)),
                ('custEmail', models.EmailField(max_length=254, verbose_name='email address')),
                ('custPhone', models.CharField(default='0000000000', max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('address', models.CharField(max_length=255)),
                ('productNumber', models.CharField(max_length=100)),
                ('expiryDate', models.DateField()),
                ('amount', models.CharField(max_length=100)),
                ('message', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
