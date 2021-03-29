from django.shortcuts import render
from core.models import Event
# Create your views here.


def event_list(request):
   #user = request.user
    event = Event.objects.all()
    data = {'events':event}
    return render(request, 'diary.html', data)