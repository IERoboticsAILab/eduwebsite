from django import template

register = template.Library()

@register.filter
def isinstanceof(obj, class_name):
    """Check if an object is an instance of a given class name."""
    return obj.__class__.__name__ == class_name

