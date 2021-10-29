from django.contrib import admin
from homepage.models import UserProfileInfo, Item, Order, OrderItem
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
