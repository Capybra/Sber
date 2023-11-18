from django.contrib import admin
from .models import Staff
from .models import Type

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('email','password', 'staff_id')



class Staff_Type(admin.ModelAdmin):
    list_display =['name', 'id',]
    list_filter = []
    list_editable = []




admin.site.register(Type, Staff_Type)
