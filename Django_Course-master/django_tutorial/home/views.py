from ast import Return
from enum import Flag
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import BookingForm

from .models import Departments, Doctors


# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)
        

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)