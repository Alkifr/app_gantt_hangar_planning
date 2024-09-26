# ganttapp/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event, Group
from django.utils.dateparse import parse_datetime

def gantt_chart(request):
    events = Event.objects.all()
    groups = Group.objects.all()
    return render(request, 'ganttapp/gantt_chart.html', {'events': events, 'groups': groups})

@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        group_name = request.POST.get('group')
        start_date = parse_datetime(request.POST.get('start_date'))
        end_date = parse_datetime(request.POST.get('end_date'))
        status = request.POST.get('status', 'pending')  # По умолчанию 'pending'

        group, created = Group.objects.get_or_create(name=group_name)
        event = Event.objects.create(title=title, group=group, start_date=start_date, end_date=end_date, status=status)

        return JsonResponse({
            'id': event.id,
            'title': event.title,
            'group': event.group.name,
            'start_date': event.start_date.isoformat(),
            'end_date': event.end_date.isoformat(),
            'status': event.status
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def delete_event(request):
    if request.method == 'POST':
        event_id = request.POST.get('id')
        try:
            event = Event.objects.get(id=event_id)
            event.delete()
            return JsonResponse({'success': True})
        except Event.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Event does not exist'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def edit_event(request):
    if request.method == 'POST':
        event_id = request.POST.get('id')
        title = request.POST.get('title')
        group_name = request.POST.get('group')
        start_date = parse_datetime(request.POST.get('start_date'))
        end_date = parse_datetime(request.POST.get('end_date'))

        event = get_object_or_404(Event, id=event_id)
        event.title = title
        event.group, created = Group.objects.get_or_create(name=group_name)
        event.start_date = start_date
        event.end_date = end_date
        event.save()

        return JsonResponse({
            'id': event.id,
            'title': event.title,
            'group': event.group.name,
            'start_date': event.start_date.isoformat(),
            'end_date': event.end_date.isoformat()
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)