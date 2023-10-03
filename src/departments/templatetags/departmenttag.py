from django import template
from departments.models import Department

register = template.Library()

@register.inclusion_tag('departments/components/list.html')
def show_departments():
    """
    Returns list of active management.
    """
    departments = Department.objects.filter(is_active=True).order_by('title')
    return {
        'departments': departments
    }