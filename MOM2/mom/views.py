from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from models import Judge, Poster, Ratings
from django.http import HttpResponse, HttpResponseRedirect


def login(request):
        #should have login.html that has the form 
        response = render(request,"mom/login.html",{})
        return response


def auth_view(request):
        #when login button pressed auth_view is triggered by the url
        username = request.POST.get('username',"NONE")
        print username
        password = request.POST.get('password',"NONE")
        print password
        user = authenticate(username=username, password=password)
        if user is not None: 
                if user.is_active:
                        login(request,user)
                        posters = Ratings.objects.filter(judge__account__user=user)
                        response = render(request,"mom/index.html",{"posters":posters})
                else:
                        return HttpResponse("Disabled account")
        else: 
                return HttpResponse('invalid login')

def logout(request):
        print "logout called"
        return HttpResponseRedirect(reverse('index'))

#def logout(request):
#        logout(request)
        #login page has the info about the app and login form
#        return HttpResponseRedirect(reverse('login'))


@login_required
def submit(request):
        return HttpResponse("hi")
    

def index(request):
        return HttpResponse("index")
