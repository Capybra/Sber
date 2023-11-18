from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display =['user', 'name', 'phone', 'rating', 'image', 'created_at', 'updated_at']
    list_filter = ['rating', 'created_at', 'updated_at']
    list_editable = []

admin.site.register(Profile, ProfileAdmin)
