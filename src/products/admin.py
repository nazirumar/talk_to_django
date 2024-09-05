from django.contrib import admin
from products.models import Product, Embedding
# Register your models here.



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp')
    


@admin.register(Embedding)
class EmbedingAdmin(admin.ModelAdmin):
    list_display = ('embedding',
                    'object_id',
                    'content_type',
                    'content_object',)