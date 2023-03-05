from django.urls import path
from study_tracker.views import show_tracker
from study_tracker.views import add_assignment
from study_tracker.views import show_xml
from study_tracker.views import show_json

app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('add_assignment/', add_assignment, name='add_assignment'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    ]
