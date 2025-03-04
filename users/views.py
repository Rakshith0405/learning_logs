from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """registers a new page"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # log the user in and redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # display a blank or invalid form
    context = {'form':form}
    return render(request, 'registration/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('users/logged_out.html') # Redirect to your desired page after logout
