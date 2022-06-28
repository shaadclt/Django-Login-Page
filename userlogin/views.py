from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

@never_cache
@login_required(login_url='signin')
def home(request):
    return render(request,"userlogin/page.html")

@never_cache
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            
            if user is not None:
                login(request, user)
                return render(request, "userlogin/page.html")
            
            else:
                messages.error(request, "Wrong Username or Password!!!")
                return redirect('home')

    return render(request,'userlogin/signin.html')

@never_cache
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')