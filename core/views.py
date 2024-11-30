from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Venue, Guest, Wedding
from .forms import CustomUserCreationForm,VenueForm, GuestForm, WeddingForm, GuestUpdateForm, WeddingUpdateForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def update_guest(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)

    if request.user.email != guest.email:
        return redirect('event_list')
    
    if request.method == "POST":
        form = GuestUpdateForm(request.POST)
        if form.is_valid():
            status = request.POST.get('status')
            if status in ['Yes', 'No', 'Pending']:
                guest.status = status
                guest.save()
                return redirect('user-events')
    else:
        form = GuestUpdateForm(request.POST)
    
    return render(request, 'core/guest.html', {"form": form, "guest":guest})

def update_event(request, event_id):
    event = get_object_or_404(Wedding, event_id)

    if request.user != event.created_by:
        return redirect('event_list')  # Redirect if unauthorized
    
    if request.method == "POST":
        form = WeddingForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-detail', event_id=event.id)
    else:
        form = WeddingUpdateForm(instance=event)
    return render(request, 'core/update_event.html', {"form": form})

def delete_event(request, event_id):
    event = get_object_or_404(Wedding, pk=event_id)
    if event.created_by == request.user:
        event.delete()
        return redirect('user-events')
    return redirect('user-events')


def index(request):
    events = Wedding.objects.all()
    return render(request, 'core/index.html', {"events":events})

def user_events(request):
    events = Wedding.objects.all().filter(created_by=request.user)
    return render(request, 'core/user_events.html', {"events": events})

def event_detail(request, event_id):
    event = get_object_or_404(Wedding, pk=event_id)
    return render(request, 'core/event_details.html', {"event":event, "guests": event.guests.all()})

def user_events(request):
    guests = Guest.objects.filter(email = request.user.email)
    events = Wedding.objects.filter(guests__email= request.user.email)
    form = GuestUpdateForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print(form)
    return render(request, 'core/invitations.html', {"events": events, "guests": guests, "form":form})

def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'core/venue_list.html', {"venues": venues})

def add_venue(request):
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('venue-list')
    else:
        form = VenueForm()
    return render(request, 'core/venue_form.html', {"form":form})

def add_event(request):
    if request.method == "POST":
        form = WeddingForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('index')
    else:
        form = WeddingForm()
    return render(request, 'core/wedding_form.html', {"form": form})

def add_guest(request, wedding_id):
    event = get_object_or_404(Wedding, pk=wedding_id)
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save()
            event.guests.add(guest)
            event.save()
            guest.save()
            return redirect('user-events')
    else:
        form = GuestForm
    return render(request, 'core/guest_form.html', {"form": form})