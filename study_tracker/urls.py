from django.urls import path
from study_tracker.views import show_tracker
from study_tracker.views import add_assignment

app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('add_assignment/', add_assignment, name='add_assignment')
]
