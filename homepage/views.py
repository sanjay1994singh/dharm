from django.http import JsonResponse
from django.shortcuts import redirect, render
from accounts.models import EnquiryDetails
from homepage.models import LookupField
from services.models import Service

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        email = form.get('email')
        whatsapp = form.get('whatsapp')
        message = form.get('message')
        enquiry = EnquiryDetails.objects.create(name=name,email=email,whatsapp=whatsapp,message=message)
        if enquiry:
            id = enquiry.id
            status = 'success'
            msg = 'Your message sent.'
        else:
            id = 0
            status = 'faild'
            msg = 'Your message not sent.'
        json_data = {
            'id':id,
            'status':status,
            'msg':msg,
        }    
        return redirect('/')

    title_logo_data=LookupField.objects.get(code='TITLE')
    banner1 = LookupField.objects.get(code='HOME_BANNER1')
    about_data=LookupField.objects.get(code='ABOUT')
    services = Service.objects.all()[:6]
    barcode = LookupField.objects.get(code='BAR_CODE')
    shloka = LookupField.objects.filter(code='SHLOKA')
    context = {
        'title_data':title_logo_data,
        'banner1':banner1,
        'about_data':about_data,
        'services':services,
        'barcode':barcode,
        'shloka':shloka,
    }
    return render(request, 'index.html',context)

def service_details(request,id):
    title_logo_data=LookupField.objects.get(code='TITLE')
    services = Service.objects.get(id=id)

    context = {
        'services':services,
        'title_data':title_logo_data,
    }
    return render(request,'service_detail.html',context)
