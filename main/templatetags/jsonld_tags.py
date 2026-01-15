import json
from django import template

register = template.Library()


@register.filter
def jsonld_escape(value):
    """Escape a value for safe use in JSON-LD."""
    if value is None:
        return ""
    return json.dumps(str(value))[1:-1]  # Remove surrounding quotes
