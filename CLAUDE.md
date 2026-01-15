# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

```bash
# Run development server
python manage.py runserver

# Database migrations
python manage.py makemigrations  # Create new migrations
python manage.py migrate         # Apply migrations

# Admin user
python manage.py createsuperuser

# Database backup/restore
python manage.py dumpdata > backup.json
python manage.py loaddata backup.json
```

## Architecture Overview

This is a Django 5.1 academic portfolio website with a single app (`main`) containing all functionality.

### Project Structure
- `personal_site/` - Django project settings and URL routing
- `main/` - Primary app with models, views, and templates
- `templates/base.html` - Root template with navigation and HTMX setup
- `main/templates/main/` - Page templates
- `main/templates/main/partials/` - HTMX partial templates for dynamic updates
- `static/css/` - Per-page CSS files (about.css, projects.css, etc.)

### Key Models (`main/models.py`)

The site uses content models that are managed through Django Admin:

- **IntroText** - Homepage intro with CV file and social links (singleton-like)
- **SiteSettings** - Site title, subtitle, banner image (singleton pattern)
- **Publication** - Academic papers with keywords (ManyToMany)
- **Project** - Portfolio projects with slug URLs and image galleries
- **ResearchLine** - Groups projects and publications together
- **Course** - Teaching courses with syllabus files
- **EducationItem/WorkItem** - Experience timeline entries (orderable)
- **Talk** - Video talks with YouTube embeds
- **OpenPositions** - Job postings on contact page

### HTMX Integration

The site uses django-htmx for dynamic content loading:
- Views check `request.htmx` to return partials vs full pages
- Partials in `main/templates/main/partials/` for list updates
- Publications page has search/filter with HTMX

### Template Features

- **Markdown support**: `{% load markdown_extras %}` then `{{ text|markdown|safe }}`
- **Context processor**: `site_settings` available globally in all templates
- **Slug-based URLs**: Projects and ResearchLines use slugs (auto-generated from title)

### Admin Patterns

- `SiteSettings` and `ExperienceDescription` enforce singleton behavior
- `ProjectImage` uses inline editing within Project admin
- Items with `order` field use `list_editable` for drag-and-drop ordering
