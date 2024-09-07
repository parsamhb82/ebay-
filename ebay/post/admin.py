from django.contrib.admin import register, ModelAdmin
from .models import * 

@register(Post)
class PostAdmin(ModelAdmin):
    search_fields = [
        'title',
        'price',
    ]

@register(Category)
class CategoryAdmin(ModelAdmin):
    search_fields = [
        'name'
    ]

@register(Message)
class MessageAdmin(ModelAdmin):
    search_fields = [
        'timestamp'
    ]
