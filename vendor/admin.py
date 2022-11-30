from django.contrib import admin
from .models import * 

admin.site.register(VendorMaster)
admin.site.register(Order)
admin.site.register(OrderReceived)
