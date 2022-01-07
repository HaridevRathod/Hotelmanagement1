from django.contrib import admin

# Register your models here.
from .models import CustomerForm
 
@admin.register(CustomerForm)
class customer_form(admin.ModelAdmin):
  display = ['first_name', 'last_name', 'mobile_number', 'address', 'room_no', 'no_of_the_days_to_stay', 'date']

