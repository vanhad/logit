from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import User
# import jwt,datetime
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
            if User.objects.filter(first_name=username).exists():
                return HttpResponse('Username already taken')
            else:
                user = User.objects.create(email=email, password=password, last_name=addressA+' '+addressB, first_name=username)
            user.save()
        else:
            return HttpResponse('Password not matching')
        return redirect('login')

    else:
        return render(request, 'create-account.html')



def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            return HttpResponse('Username not found')

        if user.password!=password :
            return HttpResponse('Wrong Password')
        
        # return redirect('userInfo',email)
        return render(request,'userInfo.html',{'user':user})

    return render(request,'login.html')



# def userInfo(request, user_details):
#     print(user_details)
#     user = User.objects.filter(email=user_details).first()
#     useremail = user.email()
    
#     return render(request,'userInfo.html',{'email':useremail})