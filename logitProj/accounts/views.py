from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        addressA = request.POST['addressA']
        addressB = request.POST['addressB']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse('Username already taken')
            else:
                user = User.objects.create_user(email=email, password=password, last_name=addressA+addressB, username=username)
            user.save()
        else:
            return HttpResponse('Password not matching')
        return redirect('login')

    else:
        return render(request, 'create-account.html')

def login(request):
    return render(request, 'login.html')

