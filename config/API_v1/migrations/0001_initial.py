# Generated by Django 4.2.1 on 2023-05-18 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='API_v1.category')),
            ],
        ),
        migrations.CreateModel(
            name='My_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=155)),
                ('company_country', django_countries.fields.CountryField(max_length=2)),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_v1.business_type')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_v1.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('price', models.FloatField()),
                ('amount', models.PositiveIntegerField()),
                ('amount_unity', models.CharField(choices=[('tons', 'tons'), ('m3', 'm3'), ('pieces', 'pieces'), ('liters', 'liters'), ('meters', 'meters')], max_length=6)),
                ('image', models.ImageField(upload_to='images/')),
                ('orign_country', django_countries.fields.CountryField(max_length=2)),
                ('shipping_information', models.CharField(choices=[('EXW', 'EXW'), ('FCA', 'FCA'), ('FAS', 'FAS'), ('FOB', 'FOB'), ('CRF/CIF', 'CRF/CIF'), ('DPU', 'DPU'), ('DAP', 'DAP'), ('DDP', 'DDP')], max_length=7)),
                ('payment_details', models.CharField(choices=[('T/T', 'T/T'), ('L/C', 'L/C'), ('CAD', 'CAD'), ('other', 'other')], max_length=6)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_v1.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_v1.my_user')),
            ],
        ),
    ]
