from django.db import models

# Create your models here.
class Shipment(models.Model):
    STATUS = (
        ('pending', 'PENDING'),
        ('recieved', 'RECIEVED'),
        ('awaiting', 'AWAITING CLEARANCE'),
        ('in progress', 'IN PROGRESS'),
        ('in transit', 'IN TRANSIT'),
        ('shipped', 'SHIPPED'),
        ('delivered', 'DELIVERED'),
    )
    INSURANCE = (
        ('yes', 'YES'),
        ('no', 'NO'),
    )
    SHIPMENT_TYPE =(
        ('air freight', 'AIR FREIGHT'),
        ('ocean freight', 'OCEAN FREIGHT'),
        ('procurement', 'PROCUMENT'),
    )
    name = models.CharField(max_length=225, null=True)
    phone = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=300, null=True)
    email = models.EmailField(max_length=225,unique=True, null=True)
    ship_code = models.CharField(max_length=225, null=True)
    image = models.ImageField(blank=True)
    from_name = models.CharField(max_length=225, blank=True)
    from_address = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=200)
    insurance = models.CharField(max_length=50, choices=INSURANCE, default='NO')
    quantity = models.IntegerField()
    status = models.CharField(max_length=250, choices=STATUS, default='pending')
    ship_type = models.CharField(max_length=200, choices=SHIPMENT_TYPE, default='procurement')
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + "-"+ self.ship_code


class Track(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    address = models.CharField(max_length=225, blank=True)

    def __str__(self):
        return self.shipment.name
    