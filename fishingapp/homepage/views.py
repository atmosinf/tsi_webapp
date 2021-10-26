from django.shortcuts import render
from homepage.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from homepage import models
from django.views.generic import View, TemplateView, ListView, DetailView

class IndexView(ListView):
    context_object_name = 'item_list'
    model = models.Item

# Create your views here.
class ItemDetailView(DetailView):
    context_object_name = 'item_detail'
    model = models.Item
    template_name = 'homepage/item.html'

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'homepage/registration.html',
                                        {'user_form':user_form,
                                        'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'homepage/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
