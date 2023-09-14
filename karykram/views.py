from django.shortcuts import render

from .models import Karykram
from homepage.models import LookupField

# Create your views here.
def karykram(request, type):
    title_logo_data = LookupField.objects.get(code='TITLE')
    karykram = Karykram.objects.filter(type__type=type)
    context = {
        'title_data': title_logo_data,
        'karykram': karykram,
    }
    return render(request, 'karykram.html', context)
