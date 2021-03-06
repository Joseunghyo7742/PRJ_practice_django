from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method=='POST': 
        if request.POST['password1'] ==request.POST['password2']:
            user= User.objects.create_user(username= request.POST['username'], password=request.POST['password1']) #계정생성
            auth.login(request,user) #회원가입후 바로 로그인 되도록 하기 위해 
            return redirect('home')

    return render(request, 'signup.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(request, username= username, password=password) #회원이 있는지 확인해보는 것 

        if user is not None: #존재하는 회원이라면
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')
   
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
    return render(request,'login.html')