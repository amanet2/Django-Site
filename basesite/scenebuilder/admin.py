from django.contrib import admin

from .models import Map

class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['map_name']}),
        ('Map Author', {'fields': ['map_author']}),
        ('Date information', {'fields': ['map_date'], 'classes': ['collapse']}),
    ]
    list_display = ('map_name', 'map_author', 'map_date')
    list_filter = ['map_date']
    search_fields = ['map_name']

admin.site.register(Map,MapAdmin)