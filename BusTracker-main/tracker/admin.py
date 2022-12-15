from django.contrib import admin
from .models import User, Announcements, Stops, Route, Bus, BusCoordinates, Bookings,Feedback
# Register your models here.


admin.site.register(User)
admin.site.register(Announcements)
admin.site.register(Stops)
admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(BusCoordinates)
admin.site.register(Bookings)
admin.site.register(Feedback)