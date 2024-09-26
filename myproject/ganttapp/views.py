from django.shortcuts import render
from .models import Event, Group

def gantt_chart(request):
    events = Event.objects.all()
    groups = Group.objects.all()
    return render(request, 'ganttapp/gantt_chart.html', {'events': events, 'groups': groups})
