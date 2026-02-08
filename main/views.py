


from django.shortcuts import render
from django.http import HttpRequest

def home_view(request: HttpRequest):
    return render(request, 'login.html')

def home(request: HttpRequest):
    return render(request, 'home.html')


def registerForm(request: HttpRequest):
    return render(request, 'register.html')

def Aboutus(request: HttpRequest):
    return render(request, 'AboutUs.html')




from django.shortcuts import render
from .models import Courier, TrackingHistory

def track_courier(request):
    courier = None
    history = None
    error = None

    if request.method == "POST":
        t_id = request.POST.get('tracking_id')

        try:
            courier = Courier.objects.get(tracking_id=t_id)
            history = TrackingHistory.objects.filter(courier=courier)
        except Courier.DoesNotExist:
            error = "Tracking ID not found"

    return render(request, "track.html", {
        "courier": courier,
        "history": history,
        "error": error
    })







from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# રજીસ્ટ્રેશન માટે
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # રજીસ્ટર થયા પછી સીધું લોગિન થઈ જશે
            return redirect('home') # home એ તમારા URL નું name હોવું જોઈએ
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# લોગિન માટે
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') # લોગિન થયા પછી home page પર જશે
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
 



from django.shortcuts import render, redirect

def select_payment(request):
    if request.method == "POST":
        method = request.POST.get("method")

        if method == "COD":
            return render(request, "cod.html")

        elif method == "UPI":
            return render(request, "upi.html")

        elif method == "QR":
            return render(request, "qr.html")

        elif method == "PAYPAL":
            return render(request, "paypal.html")

        elif method == "GPAY":
            return render(request, "gpay.html")

    return render(request, "payment.html")



from django.shortcuts import render
from .models import Tracking

def track_order(request):
    tracking_data = None
    error = None

    if request.method == "POST":
        track_id = request.POST.get("tracking_id")
        try:
            tracking_data = Tracking.objects.get(tracking_id=track_id)
        except Tracking.DoesNotExist:
            error = "Invalid Tracking ID"

    return render(request, "track.html", {
        "tracking_data": tracking_data,
        "error": error
    })


from django.shortcuts import render, redirect
from .models import Booking

def booking(request):
    if request.method == "POST":
        Booking.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            aadhar_number=request.POST['aadhar'],
            aadhar_photo=request.FILES.get('aadhar_photo'),
            pickup_location=request.POST['pickup'],
            drop_location=request.POST['drop']
        )
        return redirect('home')

    return render(request, 'booking.html')



from django.shortcuts import render, redirect
from .models import UserRegister

def registerForm(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = UserRegister(
            username=username,
            email=email,
            password=password
        )
        user.save()   # 👈 aa line vagar DB ma store nahi thay

        return redirect('login')

    return render(request, 'register.html')

def home_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = UserRegister.objects.filter(
            username=username,
            password=password
        ).first()

        if user:
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
    

from django.shortcuts import render, redirect
from .models import Feedback

def home(request):
    context = {
        'trust_image': {'url': '/media/trust.jpg'},
        'trust_points': [
            '10+ Years of Experience',
            'Safe & Reliable Shipping',
            '24/7 Customer Support'
        ],
        'contact': {
            'phone': '+91 98765 43210',
            'email': 'support@transworld.com',
            'address': 'India'
        }
    }
    return render(request, 'home.html', context)


def feedback(request):
    if request.method == 'POST':
        Feedback.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        return redirect('home')

from django.shortcuts import render

def contact(request):
    return  render(request,'Contact_us.html')


    from django.shortcuts import render, redirect
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            message=request.POST.get('message')
        )
        return redirect('contact')  # page reload

    return render(request, 'contact_us.html')

from .models import Shipment

def track(request):
    shipment = None
    if request.method == "POST":
        tid = request.POST.get('tracking_id')
        shipment = Shipment.objects.filter(tracking_id=tid).first()

    return render(request, 'track_result.html', {'shipment': shipment})

from django.shortcuts import render

def services(request):
    return render(request, 'services.html')