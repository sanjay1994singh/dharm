from django.shortcuts import render

# Create your views here.
from .models import Pradesh, District, Nagar, NagarPadadhikari, PradeshPadadhikari, DistrictPadadhikari


def all_pradesh(request):
    pradesh_list = Pradesh.objects.all()
    context = {
        'pradesh_list': pradesh_list,

    }
    return render(request, 'sangthan_padadhikari_list.html', context)


def pradesh_list(request, id):
    pradesh_adhikari = PradeshPadadhikari.objects.filter(pradesh_id=id)
    district_list = District.objects.filter(pradesh_id=id)
    context = {
        'pradesh_adhikari': pradesh_adhikari,
        'district_list': district_list,

    }
    return render(request, 'pradesh_list.html', context)


def district_list(request, id):
    district_adhikari = DistrictPadadhikari.objects.filter(district_id=id)
    nagar_list = Nagar.objects.filter(district_id=id)
    context = {
        'district_adhikari': district_adhikari,
        'nagar_list': nagar_list,

    }
    return render(request, 'district_list.html', context)


def nagar_list(request, id):
    nagar_adhikari = NagarPadadhikari.objects.filter(nagar_id=id)
    context = {
        'nagar_adhikari': nagar_adhikari,

    }
    return render(request, 'nagar_list.html', context)
