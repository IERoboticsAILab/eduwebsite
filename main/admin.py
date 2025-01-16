from django.contrib import admin
from .models import Project, Publication, ProjectImage

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'publication_date', 'journal')
    search_fields = ('title', 'authors', 'abstract')
    list_filter = ('publication_date', 'journal')
    date_hierarchy = 'publication_date'

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of empty forms to display

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'is_ongoing', 'technologies')
    search_fields = ('title', 'description', 'technologies')
    list_filter = ('is_ongoing', 'start_date')
    filter_horizontal = ('publications',)
    inlines = [ProjectImageInline]  # Add this line to include the image upload interface
