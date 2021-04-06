from django.shortcuts import render, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('/')
        else:
            messages.error(request, "Usuario ou Senha invalido!")

    return redirect('/')


@login_required(login_url='/login/')
def event_list(request):
    user = request.user
    event = Event.objects.filter(user=user)
    data = {'events':event}
    return render(request, 'diary.html', data)

@login_required(login_url='/login/')
def event(request):
    return render(request, 'event.html')

@login_required(login_url='/login/')
def submit_event(request):
    if request.POST:
        title = request.POST.get('title')
        dt_event = request.POST.get('dt_event')
        describe  = request.POST.get('describe')
        user = request.user
        Event.objects.create(title=title,
                             dt_event = dt_event,
                             describe = describe,
                             user = user)

    return  redirect('/')