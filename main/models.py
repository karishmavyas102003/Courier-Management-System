from django.db import models

class Courier(models.Model):
    tracking_id = models.CharField(max_length=20, unique=True)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.tracking_id


class TrackingHistory(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.courier.tracking_id} - {self.status}"




        from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.email

from django.db import models

class Tracking(models.Model):
    tracking_id = models.CharField(max_length=20, unique=True)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    current_location = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tracking_id

from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)   # 📱 mobile number
    aadhar_number = models.CharField(max_length=12)  # 🆔 aadhar number
    aadhar_photo = models.ImageField(upload_to='aadhar/', null=True, blank=True)  # 📷 photo

    pickup_location = models.CharField(max_length=200)
    drop_location = models.CharField(max_length=200)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.name


from django.db import models

class UserRegister(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    tracking_id = models.CharField(max_length=100, unique=True)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.tracking_id