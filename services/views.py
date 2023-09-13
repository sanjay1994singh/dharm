from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from homepage.models import LookupField

from .models import RajatShila, Rashi, DharmikAyojan, DharmSandesh, Place, JyotishSamadhan, BrajYatraDetails, HelpLine


def jyotish(request):
    rashi = Rashi.objects.all()
    context = {
        'rashi': rashi,
    }
    return render(request, 'jyotish.html', context)


def dharm_sandesh(request):
    sandesh = DharmSandesh.objects.all().order_by('-id')[:10]

    context = {
        'sandesh': sandesh
    }
    return render(request, 'dharm_sandesh.html', context)


def dharmik_ayojan(request):
    ayojan = DharmikAyojan.objects.all()
    context = {
        'ayojan': ayojan,
    }
    return render(request, 'dharmik_ayojan.html', context)


def rajat_shila(request):
    rajat = RajatShila.objects.all()

    context = {
        'rajat': rajat,
    }
    return render(request, 'rajat_shila.html', context)


def braj_yatra(request):
    yatra = Place.objects.all().order_by('-id')[:10]
    context = {
        'yatra': yatra,
    }
    return render(request, 'braj_yatra.html', context)

def braj_yatra_place(request, id):
    yatra = BrajYatraDetails.objects.filter(place_id=id)
    context = {
        'yatra': yatra,
    }
    return render(request, 'braj_yatra_place.html', context)

def temple_details(request, id):
    yatra = BrajYatraDetails.objects.get(id=id)
    context = {
        'yatra': yatra,
    }
    return render(request, 'temple_details.html', context)

def daan(request):
    barcode = LookupField.objects.get(code='BAR_CODE')
    context = {
        'barcode': barcode,
    }
    return render(request, 'daan.html', context)


def jyotish_samadhan(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        dob = form.get('dob')
        dob = datetime.strptime(dob, '%d/%m/%Y')
        dob_place = form.get('dob_place')
        dob_time = form.get('dob_time')
        contact = form.get('mobile')
        question = form.get('question')
        obj = JyotishSamadhan.objects.create(name=name,
                                             dob=dob,
                                             dob_place=dob_place,
                                             dob_time=dob_time,
                                             contact=contact,
                                             question=question,
                                             )
        if obj:
            id = obj.id
            status = 'sent your query successfully.'
            context = {
                'id': id,
                'status': status
            }
            return JsonResponse(context)

def helpline(request):
    helpline = HelpLine.objects.all()
    context = {
        'helpline': helpline,
    }
    return render(request, 'help_line.html', context)
