from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'successfully created {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(request, 'user/signup.html', {"form": form})


@login_required()
def profile(request):
    prof = Profile.objects.filter(id=request.user.id)
    prof = prof[0]
    print(prof.user.username)
    user_data = {'username': prof.user.username, 'first_name': prof.user.first_name, 'last_name': prof.user.last_name,
                 'email': prof.user.email, 'profile_pic': prof.profile_pic}
    print(user_data)
    if request.method == "POST":

        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = dict(form.cleaned_data)
            prof.user.username = data['username']
            prof.user.first_name = data['first_name']
            prof.user.last_name = data['last_name']
            prof.user.email = data['email']
            if data['profile_pic']:
                prof.profile_pic = data['profile_pic']
            prof.user.save()
            prof.save()
            messages.success(request, f'successfully modified {prof.user.username}!')
            return redirect('index')
    else:
        form = UserProfileForm(user_data)

    return render(request, "user/profile.html", {'form': form})
