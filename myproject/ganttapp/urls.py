from django.urls import path
from . import views

urlpatterns = [
    path('gantt/', views.gantt_chart, name='gantt_chart'),
]
