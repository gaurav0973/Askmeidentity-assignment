from django.contrib import admin
from .models import Tenant, User, Product, Order

# Register your models here.

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'subdomain', 'created_on')
    search_fields = ('name', 'subdomain')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'tenant', 'is_active', 'is_admin')
    list_filter = ('role', 'tenant')
    search_fields = ('email',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'tenant')
    list_filter = ('tenant',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'tenant', 'total_amount', 'status')
    list_filter = ('status', 'tenant')