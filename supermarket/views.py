from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomerForm, OrderForm, ProductForm, CreateUserForm, UserLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Customer, Product
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

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
    item=get_object_or_404(Product,pk=pk)

    if request.method=='POST':
        form=ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewproduct')
    else:
        form=ProductForm(instance=item)
    return render(request,'editproduct.html',{'form':form})
    

@login_required
def delete_product(request,pk):
    Product.objects.filter(id=pk).delete()

    products=Product.objects.all()
    return render(request, 'viewproduct.html',{'products':products})

@login_required
def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontpage')
    else:
        form=ProductForm()
    return render(request, 'addproduct.html', {'form':form})

@login_required
def logout_page(request):
    logout('home')
    return redirect('home')

def home(request):
    return render(request,'home.html')

@login_required
def front_page(request):
    return render(request,'frontpage.html')



def register(request):
    user=request.user
    if user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+user)
                return redirect('loginpage')
        else:
            form=CreateUserForm()
        context={'form':form}
        return render(request,'register.html',context)
    
def login_page(request):
    user = request.user
    if user.is_authenticated:
        return redirect('frontpage')
    else:
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            login(request,user)
            if next:
                return redirect(next)
            return redirect('frontpage')
        context = {
            'form':form,
        }
        return render(request, 'login.html', context)

















