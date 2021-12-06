from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages

from usefulModels.getIdiom import getIdiom
from .forms import signUpForm
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import views as auth_views, login, authenticate

@never_cache
def signUp(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('signin')
    else:
        form = signUpForm()
    return render(request, 'signUp.html', {'title': 'Sign Up', 'form': form, 'idiom4Day': getIdiom()})


