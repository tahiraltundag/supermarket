from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomerForm, OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Customer, Product

@login_required
def add_customer(request):
    if request.method=='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            x=form.save()
            #pk1=form.pk
            #return redirect('addorder', pk=form.pk)
            #return redirect('frontpage')
            return HttpResponseRedirect(reverse('addorder', args=(x.pk,)))
        
    else:
        form = CustomerForm()
    return render(request,'addcustomer.html',{'form':form})
@login_required
def add_order(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form=OrderForm(instance=customer)
    if request.method=='POST':
        form=OrderForm(request.POST, instance=customer)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect(reverse('addorder', args=(customer.pk,)))

        else:
            form=OrderForm(instance=customer)
        
    x=Customer.objects.filter(pk=pk).get()
    sum=0
    for y in x.products.all():
        sum+=int(y.cost)
    return render(request, 'addorder.html',{'customer':customer,'form':form,'x':x,'sum':sum})

@login_required
def delete_order(request,a,b):
    customer = get_object_or_404(Customer, pk=b)
    product = get_object_or_404(Product, pk=a)
    if request.method=='POST':
        customer.products.remove(product)
        return redirect('addorder')
    
    return HttpResponseRedirect(reverse('addorder', args=(customer.pk,)))

@login_required
def view_customer(request):
    customer=Customer.objects.all()
    return render(request, 'viewcustomer.html',{'customer':customer})

@login_required
def view_product(request):
    products = Product.objects.all()
    return render(request, 'viewproduct.html',{'product':products})

@login_required
def edit_product(request,pk):
    



















