from django.shortcuts import render

# registration
@csrf_exempt
def index(request):
    return HttpResponse('This is main')


def login(request):
        if (request.user.is_authenticated()):
                
                response = 
                
                return HttpResponse(response)
        else:
                return HttpResponse('NULL')
def invalid_login(request):
        return HttpResponse('invalid_login')

def logout(request):
        auth.logout(request)
        return HttpResponse('logout_successful')

def submit(request):
        



