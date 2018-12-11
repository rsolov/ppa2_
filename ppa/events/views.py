from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Event, Region
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test
from .forms import NewEventForm
from django.utils import timezone


def is_riga(user):
    return user.groups.filter(name='Riga').exists()


def is_jurmala(user):
    return user.groups.filter(name='Jurmala').exists()


def objectApprove(request, pk):
    object = get_object_or_404(Event, pk=pk)
    object.delete()
    return redirect('events')


def eventsView(request):
    user = request.user
    current_user = request.user.get_username()
    if is_riga(user):
        events = Event.objects.all().filter(region__name="Riga")
        return render(request, 'staffevents.html', {'events': events})
    elif is_jurmala(user): #
        events = Event.objects.all().filter(region__name="Jurmala")
        # events = Event.objects.all().filter(region="Riga")
        return render(request, 'staffevents.html', {'events': events})
    else:
        events = Event.objects.all().filter(author=user)
        return render(request, 'events.html', {'events': events}) #events_names})


def create_event(request):
    user = User.objects.first()  # get the currently logged in user
    if request.method == 'POST':
        form = NewEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)

            print(form.cleaned_data.get('region'))
            post = Event.objects.create(
                name=form.cleaned_data.get('name'),
                region=form.cleaned_data.get('region'),
                event_name=form.cleaned_data.get('event_name'),
                location=form.cleaned_data.get('location'),
                event_date=form.cleaned_data.get('event_date'),
                #start_time=form.cleaned_data.get('start_time'),
                #end_time=form.cleaned_data.get('end_time'),
                event_desr=form.cleaned_data.get('description'),
                #event_guest_count=form.cleaned_data.get('guest_count'),
                #event_host_count=form.cleaned_data.get('host_count'),
                event_dangerous_equipment=form.cleaned_data.get('dangerous_equipment'),
                created_date=timezone.now(),
                author=user
            )
            return redirect('events')
    else:
        form = NewEventForm()
    return render(request, 'create_event.html', {'form': form})


