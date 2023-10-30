import razorpay
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from homepage.models import LookupField

from .models import CustomUser, MemberType, Gender

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


def add_member(request, id):
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

        member = MemberType.objects.get(id=id)
        mem_type = member.role

        if mem_type == 'free':
            return redirect('/account/free-member/')

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
            print(image, '==============image')
            obj.image = image
            obj.save()
            return redirect('/')

    else:
        title_logo_data = LookupField.objects.get(code='TITLE')
        banner1 = LookupField.objects.get(code='HOME_BANNER1')
        barcode = LookupField.objects.get(code='BAR_CODE')

        member_type = MemberType.objects.all()
        free_member = MemberType.objects.get(price__lt=1)
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

