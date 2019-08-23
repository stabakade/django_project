from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm, UpdateUserForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #form = UserCreationForm(request.POST)  initially we had used this form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  #cleaned_data is a dictionary
            messages.success(request, f'Account created! You can now log in')
            #return redirect('blog-home')
            return redirect('login')
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})

@login_required   #to add additional functionality
def profile(request):
    if request.method == 'POST': #if it is POST request, then we will save the user and profile data in respective variables, aslo it should be valid
        u_form = UpdateUserForm(request.POST, request.FILES, instance=request.user) #this is an instance of the current logged in user
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #we passed the request of the profile of the current logged in user
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)