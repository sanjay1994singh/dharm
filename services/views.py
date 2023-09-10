from django.shortcuts import render

from .models import RajatShila, Rashi, DharmikAyojan, DharmSandesh


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
    return render(request, 'braj_yatra.html')


def daan(request):
    return render(request, 'daan.html')
