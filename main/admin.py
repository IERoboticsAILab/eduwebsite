from django.contrib import admin
from .models import Project, Publication, ProjectImage, IntroText

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'publication_date', 'journal')
    search_fields = ('title', 'authors', 'abstract')
    list_filter = ('publication_date', 'journal')
    date_hierarchy = 'publication_date'

@admin.register(IntroText)
class IntroTextAdmin(admin.ModelAdmin):
    list_display = ('text_preview',)

    def text_preview(self, obj):
        # Return first 50 characters of the text as a preview
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Text Preview'

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of empty forms to display

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    filter_horizontal = ('publications',)
    inlines = [ProjectImageInline]  # Add this line to include the image upload interface
