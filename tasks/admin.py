from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for Task model.
    """
    list_display = ['title', 'user', 'priority', 'due_date', 'completed', 'created_at']
    list_filter = ['priority', 'completed', 'created_at', 'due_date']
    search_fields = ['title', 'description', 'user__username']
    list_editable = ['completed']
    ordering = ['-priority', 'due_date', '-created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Task Information', {
            'fields': ('user', 'title', 'description')
        }),
        ('Task Details', {
            'fields': ('priority', 'due_date', 'completed')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
