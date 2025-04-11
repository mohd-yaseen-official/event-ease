from datetime import date

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from events.models import Event
from authentication.models import Customer
from .models import Feature


def index(request):

    features = Feature.objects.all()

    context = {
        'title': 'Home Page',
        'features': features
    }
    return render(request, 'web/index.html', context)


@login_required(login_url='authentication:login')
def dashboard(request):

    customer = get_object_or_404(Customer, user=request.user)

    events = Event.objects.filter(customer=customer, is_deleted=False)

    todays_events = events.filter(customer=customer, date_and_time__date=date.today())
    
    context = {
        'title': 'Dashboard',

        'customer': customer,

        'total_events': len(events),
        'months_events': len(events.filter(date_and_time__month=date.today().month)),

        'todays_events': todays_events,
    }
    
    return render(request, 'web/dashboard.html', context)