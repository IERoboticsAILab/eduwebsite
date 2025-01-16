# Personal Website

A personal website built with Django, featuring a blog, portfolio, and internationalization support.

## 🚀 Local Development Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
```bash
git clone https://github.com/haxybaxy/eduwebsite.git
cd eduwebsite
```

2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```


4. Run database migrations
```bash
python manage.py migrate
```

5. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

The site should now be running at `http://127.0.0.1:8000/`

## 🌐 Internationalization (i18n)

### Adding New Translations

1. Mark strings for translation in your Python code:
```python
from django.utils.translation import gettext_lazy as _

message = _("This will be translated")
```

2. In templates:
```html
{% load i18n %}
{% trans "This will be translated" %}
```

3. Generate/update message files:
```bash
# Generate/update .po files
python manage.py makemessages -l es  # for Spanish

# After translating .po files, compile them
python manage.py compilemessages
```

### Working with Translations
1. Translation files are located in `locale/<language_code>/LC_MESSAGES/`
2. Edit the .po files, do not add any extra labels, just add the translations in place
3. Compile messages after making changes

## 📝 Database Management

### Migrations
Create and apply database changes:
```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations
```

### Database Backup
```bash
# Create backup
python manage.py dumpdata > backup.json

# Restore from backup
python manage.py loaddata backup.json
```
