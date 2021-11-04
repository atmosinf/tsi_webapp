from django.shortcuts import render
from homepage.forms import UserForm
from django.http import JsonResponse
import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from homepage import models
from django.views.generic import View, TemplateView, ListView, DetailView

def orderplaced(request):
    context = {'cartitems':0}
    return render(request, 'homepage/orderplaced.html', context)

def index(request):
    item_list = models.Item.objects.all()
    order, created = models.Order.objects.get_or_create()
    items = order.orderitem_set.all()
    cartitems = order.get_cart_items

    return render(request, 'homepage/item_list.html',{'item_list':item_list,'cartitems':cartitems})

# Create your views here.
class ItemDetailView(DetailView):
    context_object_name = 'item_detail'
    model = models.Item
    template_name = 'homepage/item.html'

    order, created = models.Order.objects.get_or_create()
    items = order.orderitem_set.all()
    cartitems = order.get_cart_items
    extra_context={'cartitems': cartitems}

# def itemDetails(request, pk):
#     item_detail = models.Item.objects.all()
#     return render(request,'homepage/item.html',{'item_detail':item_detail})

def updateItem(request):
    data = json.loads(request.body)
    productid = data['productid']
    action = data['action']

    print('action',action)
    print('productid',productid)

    product = models.Item.objects.get(id=productid)
    order, created = models.Order.objects.get_or_create()
    orderItem, created = models.OrderItem.objects.get_or_create(order=order, item=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def cart(request):
    order, created = models.Order.objects.get_or_create()
    items = order.orderitem_set.all()
    cartitems = order.get_cart_items
    context = {'items':items, 'order':order, 'cartitems':cartitems}
    return render(request, 'homepage/cart.html', context)

def checkout(request):
    order, created = models.Order.objects.get_or_create()
    items = order.orderitem_set.all()
    cartitems = order.get_cart_items
    context = {'items':items, 'order':order, 'cartitems':cartitems}
    return render(request, 'homepage/checkout.html', context)

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
