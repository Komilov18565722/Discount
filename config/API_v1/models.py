from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField
# Create your models here.

class Business_type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey('self', related_name='subcategories', on_delete = models.CASCADE, null= True, blank=True)

    def __str__(self):
        return f'{self.title}'


class My_user(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    company_name = models.CharField(max_length=155)
    company_country = CountryField()
    business_type = models.ForeignKey(Business_type, on_delete = models.CASCADE)
    user_category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

class Product(models.Model):
    user = models.ForeignKey(My_user, on_delete= models.CASCADE)
    title = models.CharField(max_length=255)
    about = models.TextField()
    product_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.FloatField()
    
    amount = models.PositiveIntegerField()

    CHOICES = (
        ('tons', 'tons'),
        ('m3', 'm3'),
        ('pieces', 'pieces'),
        ('liters', 'liters'),
        ('meters', 'meters'),
    )
    amount_unity = models.CharField(max_length=6, choices=CHOICES)
    image = models.ImageField(upload_to='images/')
    orign_country = CountryField()
    shipping_CHOICES = (
        ('EXW', 'EXW'),
        ('FCA', 'FCA'),
        ('FAS', 'FAS'),
        ('FOB', 'FOB'),
        ('CRF/CIF', 'CRF/CIF'),
        ('DPU', 'DPU'),
        ('DAP', 'DAP'),
        ('DDP', 'DDP'),
    )
    shipping_information =  models.CharField(max_length=7, choices=shipping_CHOICES)
    payment_CHOICES = (
        ('T/T','T/T'),
        ('L/C','L/C'),
        ('CAD','CAD'),
        ('other','other'),
    )
    payment_details = models.CharField(max_length=6, choices=payment_CHOICES)

    def __str__(self):
        return f'{self.title}'