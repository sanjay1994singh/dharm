import os
import tempfile

import razorpay
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from homepage.models import LookupField

from .models import CustomUser, MemberType, Gender

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse, FileResponse
import io
from xhtml2pdf import pisa

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def certificate_genrate(request, id):
    back_image = LookupField.objects.get(code='back_image')  # Retrieve the back_image URL from your model
    back_image = request.build_absolute_uri(back_image.img.url)
    obj = CustomUser.objects.get(id=id)
    name = obj.fullname
    image = request.build_absolute_uri(obj.image.url)
    member_type = obj.member_type.type
    context = {
        'back_image': back_image,
        'width_height': "width: 100%; height: auto;",
        'name': name,
        'role': member_type,
        'user_image': image,
    }

    return render(request, 'new_certificate.html', context)


#
# def generate_pdf(html_content, output_path):
#     """
#     Generate a PDF file from HTML content and save it to the specified path using pisa.
#     """
#     with open(output_path, 'w+b') as pdf_file:
#         pisa.CreatePDF(html_content, dest=pdf_file)
#
#
# def certificate_genrate(request):
#     back_image = LookupField.objects.get(code='back_image')  # Retrieve the back_image URL from your model
#     back_image = back_image.img.url
#     print(back_image,'==============back_image')
#     context = {
#         'back_image': back_image,
#         'name': "sanjay singh",
#         'role': "Software developer"
#     }
#
#     html_content = render_to_string('new_certificate.html', context)
#
#     # Create a temporary PDF file
#     with tempfile.NamedTemporaryFile(delete=False) as pdf_file:
#         pdf_output_path = pdf_file.name
#
#         # Generate the PDF
#         generate_pdf(html_content, pdf_output_path)
#
#     # Create the EmailMessage object without text_content
#     subject = 'Your Email Subject'
#     from_email = 'mrctherapy2023@gmail.com'
#     to_email = 'srbc500@gmail.com'
#
#     email_message = EmailMessage(
#         subject,
#         '',
#         from_email,
#         [to_email],
#         headers={'Message-ID': 'foo'},
#     )
#
#     # Attach the PDF file
#     with open(pdf_output_path, 'rb') as pdf_file:
#         email_message.attach('output.pdf', pdf_file.read(), 'application/pdf')
#
#     # Send the email
#     email_message.send()
#
#     # Delete the temporary PDF file
#     os.remove(pdf_output_path)
#
#     return HttpResponse('Email sent successfully')


def generate_pdf_and_send_email():
    # Render HTML template
    back_image = LookupField.objects.get(code='back_image')  # Retrieve the back_image URL from your model
    back_image = back_image.img.url  # Get the URL of the image
    print(back_image, '=============back_image')  # Print for debugging purposes
    context = {
        'back_image': back_image,  # Pass the back_image URL to the template context
    }
    html_content = render_to_string('new_certificate.html', context)  # Render the HTML template with the context

    # Convert HTML to PDF
    result = io.BytesIO()  # Create a BytesIO object to store the PDF
    pdf = pisa.pisaDocument(io.BytesIO(html_content.encode("UTF-8")), result)  # Convert HTML to PDF
    if not pdf.err:  # If PDF generation is successful
        # Prepare email
        email = EmailMessage(
            'Subject',  # Specify email subject
            'Message Body',  # Specify email body
            'mrctherapy2023@gmail.com',  # Specify sender email
            ['srbc500@gmail.com'],  # Specify recipient email(s)
        )
        email.attach('document.pdf', result.getvalue(), 'application/pdf')  # Attach the PDF to the email
        email.send()  # Send the email

        # Return the PDF as a response
        response = FileResponse(io.BytesIO(result.getvalue()), as_attachment=True, filename='document.pdf')
        return response
    else:
        return HttpResponse('Error generating PDF and sending email: {}'.format(
            pdf.err))  # Return error message if PDF generation fails


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
    title_logo_data = LookupField.objects.get(code='TITLE')

    member = MemberType.objects.get(type=type)
    mem_type = member.role
    mem_type_id = member.id

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
        'order_id': order_id,
        'member_type': member_type,
        'member_price': amount,
        'gender_type': gender_type,
        'mem_name': mem_name,
        'type': type,
        'mem_type_id': mem_type_id,
    }
    print(order_id, '===order_id')
    return render(request, 'add_member.html', context)


def add_form_data(request):
    if request.method == 'POST':
        form = request.POST
        mem_name = form.get('mem_name')
        mem_type_id = form.get('mem_type_id')
        name = form.get('name')
        mobile = form.get('mobile')
        address = form.get('address')
        city = form.get('city')
        district = form.get('district')
        state = form.get('state')
        country = form.get('country')
        image = request.FILES.get('image')
        order_id = form.get('razorpay_order_id')
        razorpay_signature = form.get('razorpay_signature')
        payment_id = form.get('razorpay_payment_id')
        payment_status = form.get('payment_status')
        price = form.get('price')
        obj = CustomUser.objects.create(fullname=name,
                                        mobile=mobile,
                                        address=address,
                                        city=city,
                                        district=district,
                                        state=state,
                                        country=country,
                                        order_id=order_id,
                                        transaction_id=razorpay_signature,
                                        payment_id=payment_id,
                                        payment_status=payment_status,
                                        price=price,
                                        member_role=mem_name,
                                        member_type_id=mem_type_id
                                        )
        if obj:
            obj.image = image
            obj.save()
            id = obj.id
            status = 1
            context = {
                'id': id,
                'status': status
            }
            return JsonResponse(context)

def free_member(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        mobile = form.get('mobile')
        address = form.get('address')
        city = form.get('city')
        district = form.get('district')
        state = form.get('state')
        country = form.get('country')
        image = request.FILES.get('image')
        free_member = form.get('free_member')
        obj = CustomUser.objects.create(fullname=name,
                                        member_type_id=free_member,
                                        address=address,
                                        mobile=mobile,
                                        city=city,
                                        district=district,
                                        state=state,
                                        country=country,
                                        )
        if obj:
            obj.image = image
            obj.save()
            status = 1
            id= obj.id
            context = {
                'status': status,
                'id': id,
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
    title_logo_data = LookupField.objects.get(code='TITLE')
    try:
        banner1 = LookupField.objects.get(code='sadasyata')
    except:
        banner1 = ''
    free_cus = CustomUser.objects.filter(member_type__role='free')
    context = {
        'free_cus': free_cus,
        'title_data': title_logo_data,
        'banner1': banner1,
    }
    return render(request, 'sadasya_type1.html', context)


def sadasya_list2(request):
    title_logo_data = LookupField.objects.get(code='TITLE')
    try:
        banner1 = LookupField.objects.get(code='sadasyata')
    except:
        banner1 = ''
    free_cus = CustomUser.objects.filter(member_type=2)
    context = {
        'free_cus': free_cus,
        'title_data': title_logo_data,
        'banner1': banner1,
    }
    return render(request, 'sadasya_type2.html', context)


def sadasya_list3(request):
    title_logo_data = LookupField.objects.get(code='TITLE')
    try:
        banner1 = LookupField.objects.get(code='sadasyata')
    except:
        banner1 = ''
    free_cus = CustomUser.objects.filter(member_type__role=1)
    context = {
        'free_cus': free_cus,
        'title_data': title_logo_data,
        'banner1': banner1,
    }
    return render(request, 'sadasya_type2.html', context)

