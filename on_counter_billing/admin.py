from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee, Product, Customer, Bill, BillProduct
from .models import CustomUser
admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(BillProduct)
