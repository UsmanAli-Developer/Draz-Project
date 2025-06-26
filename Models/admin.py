from django.contrib import admin
from .models import Products,ProductGalleryImage,UserProfile

admin.site.register(UserProfile)
class ProductGalleryImageInline(admin.TabularInline):
    model = ProductGalleryImage
    extra = 1
    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_category', 'product_description', 'product_price', 'product_image']
    inlines = [ProductGalleryImageInline] 

admin.site.register(Products, ProductsAdmin)



