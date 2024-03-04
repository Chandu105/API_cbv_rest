from django.db import models

# Create your models here.
class Product_catogery(models.Model):
    product_catogery_id=models.IntegerField(primary_key=True)
    product_catogery_name=models.CharField(max_length=100)

    def __str__(self):
        return self.product_catogery_name
    

class Product(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_brand=models.CharField(max_length=100)
    product_catogery_id=models.ForeignKey(Product_catogery,on_delete=models.CASCADE)

    


