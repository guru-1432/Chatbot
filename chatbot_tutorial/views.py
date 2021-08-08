from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout 
from . import models

def chat(request):
    context = {'curentuser': 'harry'}
    current_user = request.user.username
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }  

    result_message = {
        'type': 'text'
    }
    if 'fat' in message['text']:
        result_message['text'] = random.choice(jokes['fat'])
    
    elif 'stupid' in message['text']:
        result_message['text'] = random.choice(jokes['stupid'])
    
    elif 'dumb' in message['text']:
        result_message['text'] = random.choice(jokes['dumb'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    return result_message
    

def loginpage(request):
    context= {}
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(username= username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Login success start chatting")
            return render(request,'chatbot_tutorial/chatbot.html')
        else:
            messages.warning(request, "Invalid username or password ") 
            return render(request,'chatbot_tutorial/login.html')
    return render(request,'chatbot_tutorial/login.html')

def logoutpg(request):
    logout(request)
    return render (request,'chatbot_tutorial/login.html')


def signup(request):
    form = UserCreationForm()
    context= {'form':form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created")
            return render(request,'chatbot_tutorial/login.html')
    return render(request,'chatbot_tutorial/signup.html',context)


def track_count(user):
    if user:
        count = 5
        current = models.UserCalls.objects.filter(Username = user).values_list()
        if current:
            count = current[0][1] +1
            update_entry = models.UserCalls.objects.filter(Username = user).update(count = count)
        else:
            new_entry =models.UserCalls(user,1)
            new_entry.save()

def showcount(request):
    result = models.UserCalls.objects.all().values_list()
    context = {
        'table_data' : list(result)
    }
    return render(request,'chatbot_tutorial/showcount.html',context = context)
    
    