import json

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from main.functions import generate_form_errors
from .forms import *


def login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                
                return HttpResponseRedirect(reverse('web:dashboard'))

        context = {

            'title': 'Login',
            'error': True,
            'message': "Invalid username or password"

        }

        return render(request, 'authentication/login.html', context)
    
    else:
        
        context = {
            'title': 'Login'
        }

    return render(request, 'authentication/login.html', context)


def logout(request):

    auth_logout(request)
    return HttpResponseRedirect(reverse('web:index'))


def create_user(request):

    if request.method == 'POST':

        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            User.objects.create_user(
                username = user.username,
                password = user.password,
                email = user.email,
                first_name = user.first_name,
                last_name = user.last_name,
            )
       
            user = authenticate(username=user.username, password=user.password)

            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('authentication:create_customer'))
            
        else:
            message = generate_form_errors(form)

            form = UserForm()

            context = {
                'title': 'Signup',
                'form': form,
                'error': True,
                'message': message
            }
            
    else:
        form = UserForm()

        context = {
            'title': 'Signup',
            'form': form,
            'page_id': 'signup_user'
        }

    return render(request, 'authentication/signup.html', context)
        

def create_customer(request):
    
    if request.method == 'POST':

        form = CustomerForm(request.POST, request.FILES)

        if form.is_valid():
            customer = form.save(commit=False)
            
            name = f'{request.user.first_name} {request.user.last_name}'

            Customer.objects.create(
                name=name,
                phone=customer.phone,
                date_of_birth=customer.date_of_birth,
                address=customer.address,
                profile_image=customer.profile_image,
                user=request.user,
            )
            
            if customer is not None:

                response_data = {
                    "message": "You have been Registered Successfully...",
                    "status": "success",
                    "title": "Registration Success",
                    "redirect": True,
                    "redirect_url": "/dashboard",
                }

                return HttpResponse(json.dumps(response_data))
            
        else:
            message = generate_form_errors(form)

            response_data = {
                    "message": str(message),
                    "status": "error",
                    "title": "Registration Failed",
                    "redirect": False,
                    "redirect_url": "",
            }

            return HttpResponse(json.dumps(response_data))
        
    else:
        if request.user and not Customer.objects.filter(user=request.user).exists():
            
            form = CustomerForm()

            context = {
                'title': 'Signup',
                'form': form,
                'page_id': 'signup_customer'
            }
            return render(request, 'authentication/signup.html', context)
    
    return render(request, 'authentication/authentication-failed.html')