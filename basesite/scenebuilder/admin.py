from django.contrib import admin

from .models import Map, Scene

class SceneInLine(admin.TabularInline):
    model = Scene
    extra = 0

class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['map_name']}),
        ('Map Author', {'fields': ['map_author']}),
        ('Date information', {'fields': ['map_date']}),
        ('File information', {'fields': ['map_path']}),
    ]
    inlines = [SceneInLine]
    list_display = ('map_name', 'map_author', 'map_date', 'map_path')
    list_filter = ['map_date']
    search_fields = ['map_name','map_author','map_path']

class SceneAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['scene_name']})
    ]
    search_fields = ['scene_name']

admin.site.register(Map,MapAdmin)
admin.site.register(Scene,SceneAdmin)