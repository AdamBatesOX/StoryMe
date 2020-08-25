from django.contrib import admin

# Register your models here.
from .models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Story

admin.site.register(Story, StoryAdmin)