from django.shortcuts import render


# Create your views here.
def puja_form(request):
    return render(request, 'puja_form.html')

def Jyotish_form(request):
    return render(request, 'jyotish_form.html')
