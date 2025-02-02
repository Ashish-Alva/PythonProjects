from django.contrib import admin
from .models import Customer 

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'Email','CreatedAt')
    search_fields = ('FirstName', 'LastName', 'Email')
    list_filter = ('Email','CreatedAt')

admin.site.register(Customer,CustomerAdmin)