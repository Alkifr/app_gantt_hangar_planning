from django.urls import path
from . import views

urlpatterns = [
    path('gantt/', views.gantt_chart, name='gantt_chart'),
    path('add-event/', views.add_event, name='add_event'),
    path('delete-event/', views.delete_event, name='delete_event'),
    path('edit-event/', views.edit_event, name='edit_event'),
]
