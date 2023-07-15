import razorpay
from django.shortcuts import render
from .models import CustomUser,MemberType,Gender
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.

def join_member(request):
    member_type = MemberType.objects.all()
    context = {
        'member_type':member_type
    }
    return render(request,'join_member.html',context)


def add_member(request,id):
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
        obj = CustomUser.objects.create(name=name,
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
                                        member_type_id=member_type,
                                        id_number=id_number,
                                        )
    else:
        member = MemberType.objects.get(id=id)
        mem_type = member.type
        if mem_type == 'हितचिंतक':
            return redirect('/account/free-member/')
        
        member_type = MemberType.objects.all()
       
        gender_type = Gender.objects.all()
        amount = member.price

        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment = client.order.create({'amount': int(amount) * 100, 'currency': 'INR', 'payment_capture': '1'})
        order_id = payment['id']

        context = {
            'payment':payment,
            'member_type':member_type,
            'member_price':amount,
            'gender_type':gender_type,
        }
        return render(request,'add_member.html',context)
    
def free_member(request):
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
        obj = CustomUser.objects.create(name=name,
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
                                        # member_type_id=member_type,
                                        id_number=id_number,
                                        )
    else:
        member_type = MemberType.objects.all()
        context = {
            'member_type':member_type
        }
        return render(request,'free_member.html',context)

def success(request):
    if request.method == 'GET':
        form = request.GET
        razorpay_order_id = form.get('razorpay_order_id', None)
        razorpay_payment_id = form.get('razorpay_payment_id', None)
        razorpay_signature = form.get('razorpay_signature', None)
        price = form.get('price', None)
        payment_status = form.get('payment_status', None)
        try:
            pass
        except Exception as e:
            print(e, '=====================error in payment success function')

        if course_obj:
            msg = 'success'
        else:
            msg = 'failed'

        json_data = {'msg': msg}

        return JsonResponse(json_data)
