from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    name=models.CharField(max_length=50)
    email=models.EmailField(blank=True,null=True)
    phone=models.CharField(max_length=50,blank=True,null=True)

    def__str__(self):
        return str(self.name)

class Menu(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    def __str__(self):
        return str(self.name)

class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")
    total_amount=models.DecimalField(max_digits=8,decimal_places=2)
    def __str__(self.customer)