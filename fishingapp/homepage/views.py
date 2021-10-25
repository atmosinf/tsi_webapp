from django.shortcuts import render
from homepage.forms import UserForm

# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')

def item(request):
    return render(request, 'homepage/item.html')

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
