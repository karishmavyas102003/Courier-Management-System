from django.contrib import admin
from .models import Tracking
from .models import  Booking
from .models import UserRegister 
from .models import Feedback
from .models import Shipment




class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'mobile',
        'aadhar_number',
        'pickup_location',
        'drop_location',
        'status',
        'booking_date',
    )
    search_fields = ('name', 'mobile', 'aadhar_number')
    list_filter = ('status', 'booking_date')

admin.site.register(Booking, BookingAdmin)
admin.site.register(Tracking)
admin.site.register(UserRegister)
admin.site.register(Feedback)
admin.site.register(Shipment)



from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'created_at')