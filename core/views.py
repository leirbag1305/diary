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
            return redirect('/')
        else:
            messages.error(request, "Usuario ou Senha invalido!")

    return redirect('/')


@login_required(login_url='/login/')
def event_list(request):
    user = request.user
    event = Event.objects.filter(user=user)
    data = {'events': event}
    return render(request, 'diary.html', data)


@login_required(login_url='/login/')
def event(request):
    id_event = request.GET.get('id')
    date = {}
    if id_event:
        date ['event'] = Event.objects.get(id=id_event)
    return render(request, 'event.html', date)


@login_required(login_url='/login/')
def submit_event(request):
    if request.POST:
        title = request.POST.get('title')
        dt_event = request.POST.get('dt_event')
        describe = request.POST.get('describe')
        locale = request.POST.get('locale')
        user = request.user
        id_event = request.POST.get('id_event')
        if id_event:
            Event.objects.filter(id=id_event).update(title=title,
                                                     dt_event=dt_event,
                                                     describe=describe,
                                                     locale=locale)
        else:
            Event.objects.create(title=title,
                                 dt_event=dt_event,
                                 describe=describe,
                                 locale=locale,
                                 user=user)

    return redirect('/')

@login_required(login_url='/login/')
def delete_event(request, id_event):
    user = request.user
    event = Event.objects.get(id=id_event)
    if user == event.user:
        event.delete()

    return redirect('/')

