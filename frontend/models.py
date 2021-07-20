from django.db import models

# Create your models here.
class Shipment(models.Model):
    STATUS = (
        ('pending', 'PENDING'),
        ('in progress', 'IN PROGRESS'),
        ('shipped', 'SHIPPED'),
        ('recieved', 'RECIEVED'),
    )
    INSURANCE = (
        ('YES'),
        ('NO'),
    )
    name = models.CharField(max_length=225, null=True)
    phone = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=300, null=True)
    email = models.EmailField(max_length=225,unique=True, null=True)
    ship_code = models.CharField(max_length=225, null=True)
    image = models.ImageField()
    from_address = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=5)
    insurance = models.CharField(max_length=50, choices=INSURANCE)
    quantity = models.IntegerField(min)
    status = models.CharField(max_length=250, choices=STATUS, default='pending')
    date_order = models.DateTimeField(auto_now_add=True)


class Track(models.Model):

    shipment = models.ForeignKey(Shipment)
    address = models.CharField(max_length=225, blank=True)
    