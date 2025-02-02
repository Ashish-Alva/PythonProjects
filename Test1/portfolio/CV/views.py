from django.shortcuts import render, redirect
from .models import Customer
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        print("gfhf")
        firstname = str(request.POST.get('firstname'))
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')


        newCustomer = Customer(FirstName=firstname, LastName=lastname, Email=email)

        # Save the object to the database
        newCustomer.save()

        
        return redirect('index')
    else:
        context = {
            'name': 'Ashish',
        }
        return render(request, 'cv/index.html', context=context)