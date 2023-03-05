from django.shortcuts import render
from study_tracker.models import Assignment
from django.http import HttpResponseRedirect
from study_tracker.forms import AssignmentForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_tracker(request):
    assignments = Assignment.objects.all()
    context = {
        'list_of_assignments': assignments,
        'name': 'Kemal'
    }
    return render(request, 'tracker.html', context)

def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('study_tracker:show_tracker'))
    else:
        form = AssignmentForm()
    context = {
        'form': form
    }
    return render(request, 'add_assignment.html', context)

def show_xml(request):
    assignments = Assignment.objects.all()
    xml = serializers.serialize('xml', assignments)
    return HttpResponse(xml, content_type='text/xml')

def show_json(request):
    assignments = Assignment.objects.all()
    json = serializers.serialize('json', assignments)
    return HttpResponse(json, content_type='application/json')