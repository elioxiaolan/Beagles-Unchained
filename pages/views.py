from random import choices
from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import age_choices, gender_choices, state_choices

from listings.models import Listing
from volunteers.models import Volunteer

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'age_choices': age_choices,
        'gender_choices': gender_choices,
        'state_choices': state_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all volunteers
    volunteers = Volunteer.objects.order_by('-hire_date')

    context = {
        'volunteers': volunteers,
    }

    return render(request, 'pages/about.html', context)