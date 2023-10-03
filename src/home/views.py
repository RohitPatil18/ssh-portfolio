from django.shortcuts import render

def home(request):
    return render(request, 'home/pages/index.html')

def about(request):
    return render(request, 'home/pages/about.html')

def contacts(request):
    return render(request, 'home/pages/contacts.html')

def submit_enquiry(request):
    return render(request, 'home/pages/contacts.html')


