from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here." 
from django.http import HttpResponse
from .models import folder

@login_required(login_url="/signin")
def index(request):
    all_json_folders=folder.objects.all()
    context={'all_json_folders':all_json_folders,}
    return render(request,'index.html',context)

def signin(request):
    if request.user.is_authenticated and request.user.is_active == True :
        return redirect('/')
    if request.method == 'POST':
        user_name = request.POST['username']
        try:
            user = User.default_manager.get(username_iexact = user_name.lower())
            username = user.username
        except:
            try:
                user = User.objects.filter(email = user_name).last()
                username = user.username
            except:
                return render(request, 'signin.html', {'error' : 'User-Name/Password Invalid'})
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user == None :
            return render(request, 'signin.html', {'error' : 'User-Name/Password Invalid'})
        elif user.is_active == False :
            login(request, user)
            return redirect('/')
        else : 
            login(request, user)
            return redirect('/')
    return render(request, 'signin.html', None)

def signup(request):
    if request.user.is_active == True and request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username  = request.POST['username']
        password  = request.POST['password']
        first_name = request.POST['first_name']
        email = request.POST["email"]
        user = User.objects.create_user(username = username, first_name = first_name,email=email)
        user.set_password(password)
        user.save()
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html')

def signout(request):
    logout(request)
    return redirect('/signin')
import json
def parseData(request):
    data=request.POST["data"]
    data= json.loads(data)
    for i in data:
        fold = folder()
        fold.title= i["title"]
        fold.description= i["body"]
        fold.save()
    return redirect("/")