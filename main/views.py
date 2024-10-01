import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import TokoSepatuMuslimForm
from main.models import TokoSepatuMuslim

@login_required(login_url='/login')
# Create your views here.
def show_main(request):
    to_cart = TokoSepatuMuslim.objects.filter(user=request.user)

    context = {
        'name' : request.user.username,
        'price': 'Rp300.000',
        'description': 'Sepatu ini dibuat menggunakan bahan yang bagus, serta produk original',
        'stock' : '15',
        'to_cart': to_cart,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_to_cart(request):
    form = TokoSepatuMuslimForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        add_cart = form.save(commit=False)
        add_cart.user = request.user
        add_cart.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_to_cart.html", context)

def show_xml(request):
    data = TokoSepatuMuslim.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = TokoSepatuMuslim.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = TokoSepatuMuslim.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = TokoSepatuMuslim.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
