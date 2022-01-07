from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import CustomerForm
from .forms import MyForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm

def register_request(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth.login(request, user)
      messages.success(request, "Registration successful." )
      return redirect("ulogin")
    messages.error(request, "Unsuccessful registration. Invalid information.")
  form = NewUserForm()
  return render (request=request, template_name="register.html", context={"register_form":form})


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('/home')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'login.html')

def ulogin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('/uhome')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('ulogin')
  else:
    return render(request, 'ulogin.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('login')

def ulogout(request):
    if request.method == 'POST':
        auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('ulogin')

def home(request):
  return render (request, "home.html")

def uhome(request):
  return render (request, "uhome.html")

def about(request):
  return render (request, "about.html")

def thankyou(request):
  return render (request, "thankyou.html")

def index(request):
    data = CustomerForm.objects.all()

    cus = {
    "Customer": data
    }
    return render(request, "index.html", cus)

 
def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/index')
  else:
      form = MyForm()
  return render (request, 'CustomerForm.html', {'form': form})

def umy_form(request):
  if request.method == "POST":
    uform = MyForm(request.POST)
    if uform.is_valid():
        uform.save()
        return redirect('/thankyou')
  else:
      uform = MyForm()
  return render (request, 'uCustomerForm.html', {'uform': uform})

def update_delete(request):
    data = CustomerForm.objects.all()

    cus = {
    "Customer": data
    }
    return render(request, "update_delete.html", cus)

def delete_view(request,id):
    Customer= CustomerForm.objects.get(id = id)
    Customer.delete()
    return redirect('/update_delete')

def update_view(request,id):
    Customer = CustomerForm.objects.get(id = id)
    form = MyForm(request.POST,instance=Customer)
    if form.is_valid():
        form.save(commit=True)
        return redirect('/update_delete')
    return render(request,'update.html', {'Customer':Customer})

'''
def update_CustomerForm(request, first_name):
    first_name = char(first_name)
    try:
        CustomerForm_sel = CustomerForm.objects.get(id = first_name)
    except CustomerForm.DoesNotExist:
        return redirect('/index')
    CustomerForm = CustomerFormCreate(request.POST or None, instance = CustomerForm_sel)
    if CustomerForm.is_valid():
       CustomerForm.save()
       return redirect('/index')
    return render(request, 'CustomerForm/CustomerForm.html', {'update_CustomerForm':CustomerForm})

def delete_CustomerForm(request, first_name):
    first_name = int(first_name)
    try:
        CustomerForm_sel = CustomerForm.objects.get(id = first_name)
    except CustomerForm.DoesNotExist:
        return redirect('/index')
    CustomerForm_sel.delete()
    return redirect('/index')
'''
							    