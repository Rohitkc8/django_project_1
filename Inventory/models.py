from django.db import models

class product(models.Model):
    product_name= models.CharField(max_length=200,null=True)
    product_code= models.CharField(max_length=200,null=True)
    price=models.FloatField(default=0)
    isthis_food=models.FloatField(default=0)

    def __repr__(self):
        return f"{self.product_code}_{self.product_name}"
    
    def __str__(self):
        return f"{self.product_code}_{self.product_name}"

    