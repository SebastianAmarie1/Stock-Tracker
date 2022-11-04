from django.db import models

# Create your models here.
class Stock(models.Model): # creates a model named Stock with 4 types of information
    item_name = models.CharField(max_length=50)
    in_stock = models.BooleanField(default=True)
    price = models.IntegerField(default = 0)
    quantity = models.IntegerField(default = 0)
    email_of_user = models.EmailField(max_length=100)

    #convers the name to string to be displayed in the admin console.
    def __str__(self):
        return self.item_name

    #turns the information to readable information to be sent through JSON
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.item_name,
            'in_stock': self.in_stock,
            'quantity': self.quantity,
            'price': self.price,
            'email': self.email_of_user,
        }
