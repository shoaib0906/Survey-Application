from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from apps.survey.models import Survey
from django.core import validators


def frontpage(request):

    surveys = Survey.objects.all().order_by('id')[:1000]
    return  render(request, 'core/frontpage.html',{'surveys':surveys})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            
            
            login(request, user)

            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def accountred(request):
    return redirect('dashboard')

