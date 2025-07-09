from django.db import models

# Create your models here.

class Promotion(models.Model):
    description=models.CharField(max_length=100)
    discount=models.FloatField()
    

class Collection(models.Model):
    title=models.CharField(max_length=20)
    featured_product=models.ForeignKey('Product',on_delete=models.CASCADE,related_name='+')

class Product(models.Model):
   
    title=models.CharField(max_length=30)
    slug=models.SlugField(default='-')
    description=models.CharField(max_length=255)
    unit_price=models.FloatField()
    inventory=models.CharField(max_length=30)
    last_update=models.DateTimeField()
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotion)
    
    
class Customer(models.Model):
    MEMBERSHIP=[
       ('G','Gold'),
        ('B','Bronze'),
        ('S','Silver')]
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=255)  
    email=models.EmailField() 
    phone=models.CharField(max_length=15,null=True)
    birth_date=models.DateField(null=True) 
    membership=models.CharField(max_length=1,choices=MEMBERSHIP,default='S')

class Address(models.Model):
    street=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zip=models.PositiveSmallIntegerField(null=True)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    
class Order(models.Model):
    PAYMENT=[
       ('P','Pending'),
        ('C','Complete'),
        ('F','Failed')
    ]
    
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=10,choices=PAYMENT,default='P')
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)
    


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
    
class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()
    


    