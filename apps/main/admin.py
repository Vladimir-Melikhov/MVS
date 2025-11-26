from django.contrib import admin
from django.utils.html import format_html
from .models import ProjectsModel


@admin.register(ProjectsModel)
class ProjectsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'demonstration_badge', 'active_badge', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'demonstration', 'created_at']
    search_fields = ['name', 'author', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'author', 'description')
        }),
        ('Media', {
            'fields': ('poster', 'poster_2', 'poster_3', 'link')
        }),
        ('Settings', {
            'fields': ('demonstration', 'is_active', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def demonstration_badge(self, obj):
        if obj.demonstration:
            return format_html(
                '<span style="color: #10b981; font-weight: bold;">● DEMO</span>'
            )
        return format_html(
            '<span style="color: #ef4444; font-weight: bold;">● LIVE</span>'
        )
    demonstration_badge.short_description = 'Mode'
    
    def active_badge(self, obj):
        if obj.is_active:
            return format_html(
                '<span style="color: #10b981;">✓</span>'
            )
        return format_html(
            '<span style="color: #6b7280;">✕</span>'
        )
    active_badge.short_description = 'Active'
