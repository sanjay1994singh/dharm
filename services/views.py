from datetime import datetime

import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from homepage.models import LookupField

from .models import RajatShila, Rashi, DharmikAyojan, DharmSandesh, Place, JyotishSamadhan, BrajYatraDetails, HelpLine, \
    AyojanEnquiry


def jyotish(request):
    rashi = Rashi.objects.all()
    context = {
        'rashi': rashi,
    }
    return render(request, 'jyotish.html', context)


def dharm_sandesh(request):
    sandesh = DharmSandesh.objects.all().order_by('-id')[:10]

    context = {
        'sandesh': sandesh
    }
    return render(request, 'dharm_sandesh.html', context)


def dharmik_ayojan(request):
    ayojan = DharmikAyojan.objects.all()
    context = {
        'ayojan': ayojan,
    }
    return render(request, 'dharmik_ayojan.html', context)


def rajat_shila(request):
    rajat = RajatShila.objects.all()

    context = {
        'rajat': rajat,
    }
    return render(request, 'rajat_shila.html', context)


def braj_yatra(request):
    yatra = Place.objects.all().order_by('id')[:10]
    context = {
        'yatra': yatra,
    }
    return render(request, 'braj_yatra.html', context)


def braj_yatra_place(request, id):
    yatra = BrajYatraDetails.objects.filter(place_id=id)
    context = {
        'yatra': yatra,
    }
    return render(request, 'braj_yatra_place.html', context)


def temple_details(request, id):
    yatra = BrajYatraDetails.objects.get(id=id)
    print(yatra.other_img1)
    print(yatra.other_img2)
    print(yatra.other_img3)
    context = {
        'yatra': yatra,
    }
    return render(request, 'temple_details.html', context)


def daan(request):
    barcode = LookupField.objects.get(code='BAR_CODE')
    context = {
        'barcode': barcode,
    }
    return render(request, 'daan.html', context)


def jyotish_samadhan(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        dob = form.get('dob')
        dob = datetime.strptime(dob, '%d/%m/%Y')
        dob_place = form.get('dob_place')
        dob_time = form.get('dob_time')
        contact = form.get('mobile')
        question = form.get('question')
        obj = JyotishSamadhan.objects.create(name=name,
                                             dob=dob,
                                             dob_place=dob_place,
                                             dob_time=dob_time,
                                             contact=contact,
                                             question=question,
                                             )
        if obj:
            id = obj.id
            status = 'sent your query successfully.'
            context = {
                'id': id,
                'status': status
            }
            return JsonResponse(context)


def helpline(request):
    helpline = HelpLine.objects.all()
    context = {
        'helpline': helpline,
    }
    return render(request, 'help_line.html', context)


def ayojan_form(request, id):
    if request.method == 'POST':
        form = request.POST
        fullname = form.get('name')
        email = form.get('email')
        address = form.get('address')
        mobile = form.get('mobile')
        query = form.get('query')
        # order_id = form.get('razorpay_order_id')
        # razorpay_signature = form.get('razorpay_signature')
        # payment_id = form.get('razorpay_payment_id')
        obj = AyojanEnquiry.objects.create(mobile=mobile,
                                           email=email,
                                           address=address,
                                           fullname=fullname,
                                           query=query,
                                           # order_id=order_id,
                                           # transaction_id=razorpay_signature,
                                           # payment_id=payment_id
                                           )
        if obj:
            return redirect('/')





    else:
        title_logo_data = LookupField.objects.get(code='TITLE')
        ayojan = DharmikAyojan.objects.get(id=id)

        # amount = ayojan.money
        # if not amount:
        #     amount = 10
        # client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        # payment = client.order.create({'amount': int(amount) * 100, 'currency': 'INR', 'payment_capture': '1'})
        # order_id = payment['id']

        context = {
            'id': id,
            'title_data': title_logo_data, 'ayojan': ayojan,
            # 'payment': payment,
            # 'amount': amount
        }
        return render(request, 'ayojan_form.html', context)
