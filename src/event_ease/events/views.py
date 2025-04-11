import json
from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from main.decorators import allow_self
from main.functions import generate_form_errors, pagination
from authentication.models import Customer
from .forms import *


@login_required(login_url='authentication:login')
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():

            event_type = form.cleaned_data['event_type']

            if not Customer.objects.filter(user=request.user).exists():
                return render(request, 'authentication/authentication-failed.html')
            else:
                customer = request.user.customer

            type = EventType.objects.get_or_create(name=event_type.strip())

            event = form.save(commit=False)
            event.customer = customer 
            event.type = type[0]
            event.save()


            response_data = {
                "message": "Your new Event has been Added Successfully",
                "title": "Successfully Added",
                "status": "success",
                "redirect": True,
                "redirect_url": "/events/my-events"
            }

        else:
            error_message = generate_form_errors(form)

            response_data = {
                "message": str(error_message),
                "title": "Oops",
                "status": "error",
                "stable": "yes"
            }
        
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    
    else:
        form = EventForm()

        context = {
            'title': 'Add Event',
            'form': form
        }

        return render(request, 'events/add-event.html', context)
    

def my_events(request):

    now = date.today()

    events = Event.objects.filter(customer__user=request.user, is_deleted=False)

    event_types = EventType.objects.filter(id__in=events.values_list('type', flat=True)).distinct()
    

    search = request.GET.get('q')
    event_type_query = request.GET.get('type')
    date_and_time_query = request.GET.get('date_and_time')
    

    if date_and_time_query:
        if int(date_and_time_query) == 1:
            events = events.filter(date_and_time__date=now)

        elif int(date_and_time_query) == 2:
            events = events.filter(date_and_time__month=now.month)

        elif int(date_and_time_query) == 3:
            events = events.filter(date_and_time__year=now.year)

    if search:
        vector = SearchVector('title', weight='A') + SearchVector('description',  weight='B') + SearchVector('venue',  weight='C') + SearchVector('venue', weight='D')

        query = SearchQuery(search)

        events = events.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.001).order_by('-rank')

    if event_type_query:

        events = events.filter(type__id=event_type_query)

    paginator_instance = pagination(request, events, 4)
    
    context = {
        'title': 'My Events',
        'paginator_instance': paginator_instance,
        'event_types': event_types,
    }

    return render(request, 'events/my-events.html', context)


@login_required(login_url='authentication:login')
@allow_self
def view_event(request, id):

    event = get_object_or_404(Event, id=id)

    context = {
        'title': event.title,
        "event": event
    }

    return render(request, 'events/view-event.html', context)

    
@login_required(login_url='authentication:login')
@allow_self
def delete_event(request, id):

    event = get_object_or_404(Event, id=id)

    event.is_deleted = True
    event.save()
    
    response_data = {
        "message": "Your Event has been Deleted Successfully",
        "title": "Successfully Deleted",
        "status": "success",
        "redirect": False,
        "redirect_url": ''
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required(login_url='authentication:login')
@allow_self
def edit_event(request, id): 

    event = get_object_or_404(Event, id=id)
                                                 
    if request.method == 'POST':
        
        form = EventForm(request.POST, instance=event)

        if form.is_valid():

            event_type = form.cleaned_data['event_type']

            type = EventType.objects.get_or_create(name=event_type.strip())
            
            event = form.save(commit=False)
            event.type = type[0]
            event.save()

            response_data = {
                "message": "Your Event has been Edited Successfully",
                "title": "Successfully Edited",
                "status": "success",
                "redirect": True,
                "redirect_url": '/events/my-events'
            }

        else:
            error_message = generate_form_errors(form)

            response_data = {
                "message": str(error_message),
                "title": "Oops",
                "status": "error",
            }
        
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    
    else:
        form = EventForm(instance=event, initial={'event_type': event.type.name})

        context = {
            'title': 'Edit Event',
            'form': form
        }

        return render(request, 'events/add-event.html', context)