from django.shortcuts import render

# Create your views here.
from .models import MatraPradeshPadadhikari, MatraNagarPadadhikari, MatraDistrictPadadhikari
from sangthan_suchi.models import Pradesh, District, Nagar


def all_pradesh(request):
    pradesh_list = Pradesh.objects.all()
    context = {
        'pradesh_list': pradesh_list,

    }
    return render(request, 'matra_sangthan_padadhikari_list.html', context)


def pradesh_list(request, id):
    pradesh_adhikari = MatraPradeshPadadhikari.objects.filter(pradesh_id=id)
    district_list = District.objects.filter(pradesh_id=id)
    context = {
        'pradesh_adhikari': pradesh_adhikari,
        'district_list': district_list,

    }
    return render(request, 'matra_pradesh_list.html', context)


def district_list(request, id):
    district_adhikari = MatraDistrictPadadhikari.objects.filter(district_id=id)
    nagar_list = Nagar.objects.filter(district_id=id)
    context = {
        'district_adhikari': district_adhikari,
        'nagar_list': nagar_list,

    }
    return render(request, 'matra_district_list.html', context)


def nagar_list(request, id):
    nagar_adhikari = MatraNagarPadadhikari.objects.filter(nagar_id=id)
    context = {
        'nagar_adhikari': nagar_adhikari,

    }
    return render(request, 'matra_nagar_list.html', context)
