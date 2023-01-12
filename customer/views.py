from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm
def index(request):
    customers = Customer.objects.all()
    return render(request, 'crm/index.html', {'customers': customers})

def createCustomer(request):
    customer = CustomerForm()
    if request.method == 'POST':
        # data = CustomerForm(request.POST or None, request.FILES)
        name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        data = Customer.objects.create(customer_name=name, phone=phone, email=email,password=password)
        return redirect('index')
        # if data.is_valid():
        #     data.save()
        #     return redirect('index')
        # else:
        #     return HttpResponse(""" Something went wrong please Reload web page""")
    else:
        return render(request, 'crm/add_customer.html', {'customer_form': customer})
def selectData(request, id):
    data = Customer.objects.get(id = id)
    return render(request, 'crm/update_customer.html', {'customer': data})

def updateCustomer(request):
    if request.method == 'POST':
        id = request.POST['customer_id']
        name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        customer_data = Customer.objects.get(id=id)
        customer_data.customer_name = name
        customer_data.phone = phone
        customer_data.email = email
        customer_data.password = password
        customer_data.save()
        return redirect('index')

def delete(request, id):
    data = Customer.objects.get(id = id)
    data.delete()
    return redirect('index')
