from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    sms_code = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    marketing_opt_in = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

 
class Products(models.Model):
  product_id =models.IntegerField(unique=True)
  product_name=models.CharField(max_length=50)
  product_category=models.CharField(max_length=10)
  product_description=models.TextField()
  product_price=models.IntegerField()
  product_image=models.ImageField(upload_to='Products/')


class ProductGalleryImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='Products/gallery/')

    def __str__(self):
        return f"Image of {self.product.product_name}"
# Create your models here.
