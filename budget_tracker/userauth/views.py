from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UserChangeForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request , "sucessfully registered")
            return redirect('home')
        else:
            messages.error(request, "Something went wrong")
        

    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }

    return render(request, 'auth/register.html', context)


def logoutview(request):
    logout(request)
    return redirect('home')

def loginview(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(username = username , password = password)
        if user is not None:
            login(request, user)
            messages.success(request , "sucessfully Logged in")
            return redirect('home')
        else:
            messages.error(request, "Credentials Invalid")


    form = AuthenticationForm()
    context = {
        'form' : form
    }

    return render(request , 'auth/login.html', context)


def edituser(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST , instance = request.user)
        form.fields = {
        'username' : form.fields['username'],
        'first_name' : form.fields['first_name'],
        'last_name' : form.fields['last_name'],
    }
        if form.is_valid():
                form.save()
                messages.success(request, "Changes Saved")
                # return redirect('home')
        else:
            messages.error(request, "Something went wrong")
    else:
        form = UserChangeForm(instance = request.user)
    form.fields = {
        'username' : form.fields['username'],
        'first_name' : form.fields['first_name'],
        'last_name' : form.fields['last_name'],
    }
    context = {
        'form' : form
    }
    return render(request, 'auth/edituser.html', context)