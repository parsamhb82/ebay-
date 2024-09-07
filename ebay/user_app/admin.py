from django.contrib.admin import register, ModelAdmin
from .models import *

@register(Customer)
class CustomerAdmin(ModelAdmin):
    search_fields = [
        'phone'
    ]
    