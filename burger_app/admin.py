from django.contrib import admin

# Register your models here.
from .models import Category,Subcategory,Product,Deals

class DealsAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Deals, DealsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Subcategory,SubcategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','available','created','updated']
    list_editable=['price','available']
    list_per_page=20
    prepopulated_fields={'slug':('name',)}
admin.site.register(Product,ProductAdmin)