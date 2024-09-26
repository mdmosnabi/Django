from django.shortcuts import render , redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
from django.contrib.auth import get_user_model
# from django.conf import settings
# User = settings.AUTH_USER_MODEL

def register_view(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Hay {username} your account create successfully")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data["password1"])
            login(request,new_user)
            return redirect('home')
    else:
        form = UserRegisterForm()
        print('not ok')
    
    contex = {
        'form':form,
    }
    return render(request,'user/sing-up.html',contex)

def login_view(request):
    err = None
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # try:
        #     user = User.objects.get(username=username)
        # except Exception as e:
        #     messages.warning(request,f'{username} dose not exit')
        #     print(e)
        #     user = None
            
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user)
            messages.warning(request,"You are logged-in now")
            return redirect('home')
        else:
            messages.warning(request,f"{username} dose't exit ereate an account")
            err = "Invalid Data "
            print(err, username, password)
        
    contex = {
        "error":err,
    }
    return render(request,'user/sing-in.html',contex)

def logout_view(request):
    logout(request)
    return redirect('sing-in')
