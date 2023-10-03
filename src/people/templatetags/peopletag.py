from django import template
from django.db.models import Prefetch, Count
from people.models import Management, Consultant
from departments.models import Department

register = template.Library()

@register.inclusion_tag('people/components/management.html')
def show_management():
    """
    Returns list of active management.
    """
    management = Management.objects.filter(is_active=True)
    return {
        'management': management
    }