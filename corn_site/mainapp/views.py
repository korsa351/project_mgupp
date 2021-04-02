from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import RefEventTypes, Customers, Events, EventRegistrations, EventReservartions


def main(request):
    path = 'mainapp/index.html'
    events = Events.objects.all()

    context = {
        'events': events,
    }

    return render(request, path, context)

