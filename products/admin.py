from django.contrib import admin
# import product to add to the admin panel
from .models import Product

admin.site.register(Product)

# Register your models here.
