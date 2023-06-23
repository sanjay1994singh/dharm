from django.http import JsonResponse
from django.shortcuts import redirect, render
from accounts.models import EnquiryDetails
from homepage.models import LookupField,Gallery
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
        shloka = LookupField.objects.filter(code='SHLOKA')
        context = {
            'title_data':title_logo_data,
            'banner1':banner1,
            'about_data':about_data,
            'parichay_data':parichay_data,
            'services':services,
            'barcode':barcode,
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

def add_gallery(request):
    if request.method == 'POST':
        form = request.POST
        code = form.get('code')
        title = form.get('title')
        description = form.get('Description')
        image_files = request.FILES.getlist('image_files')
        try:
            for i in range(len(image_files)):
                Gallery.objects.create(code=code,title=title,desc=description,img=image_files[i])
            return redirect('/')
        except Exception as e:
            print(e,'-------------e')
    else:
        return render(request, 'add_gallery.html')
    

def gallery(request):
    gallery = LookupField.objects.filter(code='gallery')
    context = {
        'gallery':gallery
    }
    return render(request, 'new_gallery.html', context)