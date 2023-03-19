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
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='study_tracker:login')
def show_tracker(request):
    assignments = Assignment.objects.all()
    context = {
        'list_of_assignments': assignments,
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login'),
        'total': Assignment.objects.filter(progress__lt=100).count(),
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
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("study_tracker:show_tracker")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response       
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('study_tracker:login'))
    response.delete_cookie('last_login')
    return redirect('study_tracker:login')

def modify_assignment(request, id):
    # Get data berdasarkan ID
    assignment = Assignment.objects.get(pk = id)

    # Set instance pada form dengan data dari assignment
    form = AssignmentForm(request.POST or None, instance=assignment)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('study_tracker:show_tracker'))

    context = {'form': form}
    return render(request, "modify_assignment.html", context)

def delete_assignment(request, id):
    # Get data berdasarkan ID
    assignment = Assignment.objects.get(pk = id)
    # Hapus data
    assignment.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('study_tracker:show_tracker'))
 