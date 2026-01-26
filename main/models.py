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