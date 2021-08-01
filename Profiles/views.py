from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import Profile
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#def profiles(request):
 #   profile = Profile.objects.all()
#
    #context = {
   #     'profiles': profile,
  #  }
 #   return render(request, 'profiles/user.html', context)

#def profile_detail(request, pk):
#    profile = get_object_or_404(Profile, pk=pk)

    #context ={
     #   'profile': profile
    #}
   # return render(request, 'profiles/profile_detail.html', context)

#def follow(request, pk):
    #profile_to_follow = get_object_or_404(Profile, pk=pk)
    #user_profile = request.user
    #data = {}
    #if profile_to_follow.follows.filter(id=user_profile.id).exists():
     #   data['message'] = "You are already following this user."
    #lse:
    #    profile_to_follow.follows.add(user_profile)
    #    data['message'] = "You are now following {}".format(profile_to_follow)
    #return JsonResponse(data, safe=False)

#def following(request):
 #   profiles = Profile.objects.filter(follows=User)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully has been created')
            return redirect('loginpage')
    
    if request.user.is_authenticated == True:
        return redirect('tweets')

    context = {
        'form': form,
    } 
    return render(request, 'profiles/register.html', context)

def loginpage(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)
        
        if user is not None :
            login(request, user)
            return redirect('tweets')
        else:
            messages.info(request, 'Username or Password is incorrect')

    if request.user.is_authenticated == True:
        return redirect('tweets')

    return render(request, 'profiles/login.html' )

@login_required(login_url='loginpage')
def logoutpage(request):
    logout(request)
    return redirect('loginpage')



@login_required(login_url='loginpage')
def home(request):
    return render(request, 'profiles/home.html')