from django.shortcuts import render
from departments.models import Department
from people.models import Consultant
from django.db.models import Prefetch, Count

def consultants(request):
    departments = Department.objects.filter(is_active=True) \
        .prefetch_related(
            Prefetch("consultant_set", Consultant.objects.filter(is_active=True), to_attr='consultants')
        ).annotate(consultant_count=Count('consultant')) \
        .filter(consultant_count__gte=1)
    return render(request, 'people/pages/consultants.html', {'departments': departments})
