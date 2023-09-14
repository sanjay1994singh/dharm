from django.shortcuts import render

from .models import Karykram


# Create your views here.
def karykram(request, type):
    karykram = Karykram.objects.filter(type=type)
    context = {
        'karykram': karykram
    }
    return render(request, 'karykram.html', context)
