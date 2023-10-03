from django.shortcuts import render

def departments(request):
    return render(request, 'departments/index.html')