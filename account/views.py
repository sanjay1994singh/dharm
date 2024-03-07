import io

import razorpay
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from homepage.models import LookupField

from .models import CustomUser, MemberType, Gender
from django.http import FileResponse, HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from xhtml2pdf import pisa
import io

def generate_pdf_and_send_email():
    # Render HTML template
    back_image = LookupField.objects.get(code='back_image')
    back_image = back_image.img.url
    print(back_image, '=============back_image')
    context = {
        'data': 'data',
        'back_image': back_image,
    }
    html_content = render_to_string('certificate.html', context)

    # Convert HTML to PDF
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html_content.encode("UTF-8")), result)
    if not pdf.err:
        # Prepare email
        email = EmailMessage(
            'Subject',
            'Message Body',
            'mrctherapy2023@gmail.com',
            ['srbc500@gmail.com'],
        )
        email.attach('document.pdf', result.getvalue(), 'application/pdf')
        email.send()
        # Return the PDF as a response
        response = FileResponse(io.BytesIO(result.getvalue()), as_attachment=True, filename='document.pdf')
        return response
    else:
        return HttpResponse('Error generating PDF and sending email: {}'.format(pdf.err))





def join_member(request):
    member_type = MemberType.objects.all()

    title_logo_data = LookupField.objects.get(code='TITLE')
    try:
        banner1 = LookupField.objects.get(code='sadasyata')
    except:
        banner1 = ''

    context = {
        'title_data': title_logo_data,
        'banner1': banner1,
        'member_type': member_type
    }
    return render(request, 'join_member.html', context)


def add_member(request, type):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        email = form.get('email')
        phone = form.get('phone')
        address = form.get('address')
        pincode = form.get('pincode')
        city = form.get('city')
        district = form.get('district')
        state = form.get('state')
        country = form.get('country')
        dob = form.get('dob')
        gender = form.get('gender')
        id_number = form.get('id_number')
        order_id = form.get('razorpay_order_id')
        razorpay_signature = form.get('razorpay_signature')
        payment_id = form.get('razorpay_payment_id')
        image = request.FILES['image']
        obj = CustomUser.objects.create(fullname=name,
                                        email=email,
                                        phone=phone,
                                        address=address,
                                        pincode=pincode,
                                        city=city,
                                        district=district,
                                        state=state,
                                        country=country,
                                        dob=dob,
                                        gender_id=gender,
                                        member_type_id=id,
                                        id_number=id_number,
                                        order_id=order_id,
                                        transaction_id=razorpay_signature,
                                        payment_id=payment_id,
                                        )
        if obj:
            obj.image = image
            obj.save()
            return redirect('/')
    else:
        title_logo_data = LookupField.objects.get(code='TITLE')

        member = MemberType.objects.get(type=type)
        mem_type = member.role

        if mem_type == 'free':
            return redirect('/account/हितचिंतक-सदस्य/')

        member_type = MemberType.objects.all()
        gender_type = Gender.objects.all()
        amount = member.price
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment = client.order.create({'amount': int(amount) * 100, 'currency': 'INR', 'payment_capture': '1'})
        order_id = payment['id']
        mem_name = member.type
        context = {
            'title_data': title_logo_data,
            'payment': payment,
            'member_type': member_type,
            'member_price': amount,
            'gender_type': gender_type,
            'mem_name': mem_name,
        }
        return render(request, 'add_member.html', context)


def free_member(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        image = request.FILES.get('image')
        email = form.get('email')
        phone = form.get('phone')
        address = form.get('address')
        pincode = form.get('pincode')
        city = form.get('city')
        district = form.get('district')
        state = form.get('state')
        country = form.get('country')
        dob = form.get('dob')
        gender = form.get('gender')
        id_number = form.get('id_number')
        free_member = form.get('free_member')
        obj = CustomUser.objects.create(fullname=name,
                                        email=email,
                                        mobile=phone,
                                        address=address,
                                        pincode=pincode,
                                        city=city,
                                        district=district,
                                        state=state,
                                        country=country,
                                        dob=dob,
                                        gender_id=gender,
                                        member_type_id=free_member,
                                        id_number=id_number,
                                        )
        if obj:
            generate_pdf_and_send_email()
            obj.save()
            status = 1
            context = {
                'status': status
            }
            return JsonResponse(context)

    else:
        title_logo_data = LookupField.objects.get(code='TITLE')
        banner1 = LookupField.objects.get(code='HOME_BANNER1')
        barcode = LookupField.objects.get(code='BAR_CODE')

        member_type = MemberType.objects.all()
        free_member = MemberType.objects.get(role='free')
        gender_type = Gender.objects.all()
        id = free_member.id
        context = {
            'title_data': title_logo_data,
            'banner1': banner1,
            'barcode': barcode,
            'member_type': member_type,
            'free_member': id,
            'gender_type': gender_type,
        }
        return render(request, 'free_member.html', context)


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_conditions(request):
    return render(request, 'term_conditions.html')


def cancellation_refund(request):
    return render(request, 'cancelation_refund.html')


def shipping_delivery(request):
    return render(request, 'shipping.html')


def sadasya_list1(request):
    free_cus = CustomUser.objects.filter(member_type__role='free')
    context = {
        'free_cus': free_cus
    }
    return render(request, 'sadasya_type1.html', context)


def sadasya_list2(request):
    free_cus = CustomUser.objects.filter(member_type=2)
    context = {
        'free_cus': free_cus
    }
    return render(request, 'sadasya_type2.html', context)


def sadasya_list3(request):
    free_cus = CustomUser.objects.filter(member_type__role=1)
    context = {
        'free_cus': free_cus
    }
    return render(request, 'sadasya_type2.html', context)
