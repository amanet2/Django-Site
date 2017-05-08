from django.contrib import admin

from .models import Question, Choice, Scene


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class SceneAdmin(admin.ModelAdmin):
    fields = ['create_date', 'scene_author', 'scene_name']
    list_display = ('scene_name','scene_author', 'create_date')
    search_fields = ['scene_name', 'scene_author']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Scene, SceneAdmin)