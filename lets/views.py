from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.http import HttpResponse

##


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("../login/")
    
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect("../")# Redirect to a success page.
        else:
            return HttpResponseRedirect("../login/")
    else:
        pass 

def login_(request):
    return render(request, template_name='lets/pages/login.html')
      
@login_required(login_url='login/')
def index_view(request):
    return render(request, template_name='lets/pages/index.html')


