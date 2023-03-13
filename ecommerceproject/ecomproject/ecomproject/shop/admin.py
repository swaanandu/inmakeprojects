from django.contrib import admin

from shop.models import Category, Product


# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,categoryadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available',]
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,productadmin)