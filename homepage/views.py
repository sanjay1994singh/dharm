from account.models import EnquiryDetails
from django.http import JsonResponse
from django.shortcuts import redirect, render
# from account.models import EnquiryDetails
from advertisement.models import Advertisement, AdsType
from homepage.models import LookupField, Gallery, SangthanType, Sangthan, Post
from services.models import Service, SixBox
from .models import ImageFolder, ImageGallery
from googleapiclient.discovery import build


# Create your views here.

def dharm_kya_hai(request):
    try:
        dharm_ki_baat = LookupField.objects.get(code='dharm_ki_baat')
    except:
        dharm_ki_baat = ''
    context = {'dharm_ki_baat': dharm_ki_baat, }
    return render(request, 'dharm_kya_hai.html', context)


def homepage(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('enq_name')
        email = form.get('enq_email')
        whatsapp = form.get('whatsapp')
        message = form.get('message')
        enquiry = EnquiryDetails.objects.create(name=name, email=email, whatsapp=whatsapp, message=message)
        if enquiry:
            id = enquiry.id
            status = 'success'
            msg = 'Your message sent.'
        else:
            id = 0
            status = 'faild'
            msg = 'Your message not sent.'
        json_data = {'id': id, 'status': status, 'msg': msg, }
        return redirect('/')

    else:
        suchana = ''
        title_logo_data = LookupField.objects.get(code='TITLE')
        try:
            mrc_add = LookupField.objects.get(code='mrc_add')
            mrc_add = mrc_add.img.url
        except:
            mrc_add = ''
        try:
            suchana = LookupField.objects.get(code='suchana')
        except:
            suchana = ''

        try:
            tv = LookupField.objects.get(code='tv')
        except:
            tv = ''

        try:
            top_banner_image = LookupField.objects.get(code='top_banner_image')
        except:
            top_banner_image = ''
        banner1 = LookupField.objects.get(code='HOME_BANNER1')
        about_data = LookupField.objects.get(code='ABOUT')
        parichay_data = LookupField.objects.filter(code='parichay')
        services = Service.objects.all()
        barcode = LookupField.objects.get(code='BAR_CODE')
        shloka = LookupField.objects.filter(code='SHLOKA')

        six_box1 = SixBox.objects.all()[:3]
        six_box2 = SixBox.objects.all()[3:6]
        type_ad1 = AdsType.objects.filter(code='gallery_one')
        type_ad2 = AdsType.objects.filter(code='gallery_two')
        if type_ad1:
            gallery_one = Advertisement.objects.filter(type_id=type_ad1[0].id)
            chunked_products = [gallery_one[i:i + 5] for i in range(0, len(gallery_one), 5)]
        else:
            gallery_one = ''

        if type_ad2:
            gallery_two = Advertisement.objects.filter(type_id=type_ad2[0].id)
        else:
            gallery_two = ''

        context = {'title_data': title_logo_data, 'banner1': banner1, 'about_data': about_data,
                   'parichay_data': parichay_data, 'services': services, 'barcode': barcode, 'shloka': shloka,
                   'suchana': suchana, 'tv': tv, 'six_box1': six_box1, 'six_box2': six_box2,
                   'gallery_one': gallery_one,
                   'gallery_two': gallery_two,
                   'chunked_products': chunked_products,
                   'mrc_add': mrc_add,
                   'top_banner_image': top_banner_image,
                   }

        return render(request, 'index.html', context)


def harame_stambh(request):
    parichay_data = LookupField.objects.filter(code='parichay')
    parichay_list = []
    for i in parichay_data:
        data_dict = {}
        data_dict['id'] = i.id
        data_dict['image'] = i.img.url
        data_dict['title'] = i.title
        parichay_list.append(data_dict)

    json_data = {
        'parichay_data': parichay_list
    }
    return JsonResponse(json_data)


def biography(request, id):
    title_logo_data = LookupField.objects.get(code='TITLE')
    biography = LookupField.objects.get(id=id)

    context = {'biography': biography, 'title_data': title_logo_data, }
    return render(request, 'biography.html', context)


def service_details(request, id):
    title_logo_data = LookupField.objects.get(code='TITLE')
    services = Service.objects.get(id=id)

    context = {'services': services, 'title_data': title_logo_data, }
    return render(request, 'service_detail.html', context)


def add_gallery(request):
    if request.method == 'POST':
        form = request.POST
        code = form.get('code')
        title = form.get('title')
        description = form.get('Description')
        image_files = request.FILES.getlist('image_files')
        try:
            for i in range(len(image_files)):
                Gallery.objects.create(code=code, title=title, desc=description, img=image_files[i])
            return redirect('/')
        except Exception as e:
            print(e, '-------------e')
    else:
        return render(request, 'add_gallery.html')


def gallery(request):
    title_logo_data = LookupField.objects.get(code='TITLE')
    gallery = Gallery.objects.filter(code='gallery')
    context = {'title_data': title_logo_data, 'gallery': gallery}
    return render(request, 'new_gallery.html', context)


def viewPdf1(request):
    try:
        patrika = LookupField.objects.get(code='patrika1')
        pdf_file_path = str(patrika.pdf.url)
        return redirect(pdf_file_path)
    except Exception as e:
        print(e, '------------------e')


def viewPdf2(request):
    try:
        patrika = LookupField.objects.get(code='patrika2')
        pdf_file_path = str(patrika.pdf.url)
        return redirect(pdf_file_path)
    except Exception as e:
        print(e, '------------------e')


def photo_gallery(request):
    title_logo_data = LookupField.objects.get(code='TITLE')
    image_folder = ImageFolder.objects.all()

    context = {'title_data': title_logo_data, 'image_folder': image_folder}
    return render(request, 'photo_gallery.html', context)


def image_folder(request, id):
    title_logo_data = LookupField.objects.get(code='TITLE')
    image_gallery = ImageGallery.objects.filter(image_folder_id=id)
    print(image_gallery, '=======================image_gallery')
    context = {'title_data': title_logo_data, 'image_gallery': image_gallery}
    return render(request, 'image_gallery.html', context)


def samachar_gallery(request):
    title_logo_data = LookupField.objects.get(code='TITLE')
    gallery = Gallery.objects.filter(code='samachar')

    context = {'title_data': title_logo_data, 'gallery': gallery}

    return render(request, 'samachar_gallery.html', context)


def sangthan_suchi(request):
    if request.method == 'POST':
        form = request.POST
        form_image = request.FILES
        name = form.get('name')
        post_name = form.get('post_name')
        image = form_image.get('image')
        address = form.get('address')
        mobile = form.get('mobile')
        obj = Sangthan.objects.create(name=name, post_id=post_name, address=address, contact=mobile)
        if obj:
            obj.image = image
            obj.save()
        return redirect('/')
    sangthan = SangthanType.objects.all()
    context = {'sangthan': sangthan, }
    return render(request, 'sangthan_suchi.html', context)


def get_sangth_padname(request):
    if request.method == 'GET':
        sangthan_id = request.GET.get('sangth_id')
        post_name = Post.objects.filter(type_id=int(sangthan_id))
        data_list = []
        for i in post_name:
            data_dict = {}
            data_dict['post_id'] = i.id
            data_dict['post_name'] = i.post_name
            data_list.append(data_dict)

        json_data = {'post_name': data_list}
        return JsonResponse(json_data)


def get_sangth(request):
    if request.method == 'GET':
        sangthan = SangthanType.objects.all()
        data_list = []
        for i in sangthan:
            data_dict = {}
            data_dict['type_id'] = i.id
            data_dict['type_name'] = i.type
            data_list.append(data_dict)

        json_data = {'post_name': data_list}
        return JsonResponse(json_data)


def sangthan_list(request, id):
    title_logo_data = LookupField.objects.get(code='TITLE')
    post_ids = Post.objects.filter(type_id=id).values_list('id', flat=True)
    list_data = Sangthan.objects.filter(post_id__in=post_ids).order_by('id')
    context = {'id': id,
               'list_data': list_data,
               'title_data': title_logo_data
               }
    return render(request, 'sangthan_data_list.html', context)


def contact(request):
    title_logo_data = LookupField.objects.get(code='TITLE')
    try:
        banner1 = LookupField.objects.get(code='sampark')
    except:
        banner1 = ''
    context = {'title_data': title_logo_data, 'banner1': banner1, }
    return render(request, 'contact_us.html', context)


def add_gallery_folder(request):
    if request.method == 'POST':
        form = request.POST
        form1 = request.FILES
        image_folder_id = form.get('image_folder_id')
        image_files = form1.getlist('image_files')

        try:
            for i in range(len(image_files)):
                ImageGallery.objects.create(image_folder_id=image_folder_id,
                                            img=image_files[i])
        except Exception as e:
            print(e, '========e=========')
        return redirect('/add_gallery_folder/')
    image_folder = ImageFolder.objects.all()
    context = {
        'image_folder': image_folder
    }
    return render(request, 'add_folder_gallery.html', context)


def videos_list(request):
    video_length = LookupField.objects.filter(code='video_length')
    if video_length:
        video_length = video_length[0].desc
    else:
        video_length = 9
    api_key = 'AIzaSyCJQ2WoCt9gMmdKlkaRS_NqEyNeNyxDm9k'
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get the latest videos from a specific channel (replace 'CHANNEL_ID' with your channel ID)
    channel_id = 'UCEU4cxBUEz60ye-NUz6gSAA'
    response = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        order='date',
        type='video',
        maxResults=video_length  # You can adjust the number of videos to retrieve
    ).execute()

    videos = response.get('items', [])

    title_logo_data = LookupField.objects.get(code='TITLE')
    try:
        banner1 = LookupField.objects.get(code='sampark')
    except:
        banner1 = ''
    context = {
        'title_data': title_logo_data,
        'banner1': banner1,
        'videos': videos,
    }

    return render(request, 'videos_list.html', context)
