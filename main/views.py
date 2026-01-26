

# Create your views here.
# # myapp/views.py
# from django.shortcuts import render
# from django.http import HttpRequest

# def loginpage(request: HttpRequest):
#     # The render function takes the request object, the template name, 
#     # and an optional dictionary of context data.
#     return render(request, 'meet.html')
# myapp/views.py
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