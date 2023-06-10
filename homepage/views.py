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
    
    else:
        title_logo_data=LookupField.objects.get(code='TITLE')
        banner1 = LookupField.objects.get(code='HOME_BANNER1')
        about_data=LookupField.objects.get(code='ABOUT')
        parichay_data=LookupField.objects.filter(code='parichay')
        services = Service.objects.all().order_by('-id')
        barcode = LookupField.objects.get(code='BAR_CODE')
        # motive = LookupField.objects.get(code='motive')
        # motive = 'mmmmmmmmmmmmmm'
        shloka = LookupField.objects.filter(code='SHLOKA')
        context = {
            'title_data':title_logo_data,
            'banner1':banner1,
            'about_data':about_data,
            'parichay_data':parichay_data,
            'services':services,
            'barcode':barcode,
            # 'motive':motive,
            'shloka':shloka,
        }
        return render(request, 'index.html',context)

def biography(request,id):
    title_logo_data=LookupField.objects.get(code='TITLE')
    biography = LookupField.objects.get(id=id)

    context = {
        'biography':biography,
        'title_data':title_logo_data,
    }
    return render(request,'biography.html',context)

def service_details(request,id):
    title_logo_data=LookupField.objects.get(code='TITLE')
    services = Service.objects.get(id=id)

    context = {
        'services':services,
        'title_data':title_logo_data,
    }
    return render(request,'service_detail.html',context)
