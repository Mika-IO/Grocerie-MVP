from django.contrib import admin
from .models import Market, Product, Order, BaseConfiguration


class BaseConfigurationAdmin(admin.ModelAdmin):
    pass


class MarketAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Market, MarketAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(BaseConfiguration, BaseConfigurationAdmin)