from django.shortcuts import render
from study_tracker.models import Assignment
from django.http import HttpResponseRedirect
from study_tracker.forms import AssignmentForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='study_tracker:login')
def show_tracker(request):
    assignments = Assignment.objects.all()
    context = {
        'list_of_assignments': assignments,
        'name': request.user.username,
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('study_tracker:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('study_tracker:show_tracker')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('study_tracker:login')