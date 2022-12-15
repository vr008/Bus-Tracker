from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_view, name="logout" ),
    path('announcements', views.announcements, name="announcements"),
    path('feedback', views.feedback, name="feedback"),
    path('tracker', views.tracker, name="tracker"),
    path('bookings', views.bookings, name="bookings"),
    path('addwbus', views.addwbus, name="addwbus"),
    path('addannouncement', views.addannouncement, name="addannouncement"),
    path('addfeedback', views.addfeedback, name="addfeedback"),
    path('routes', views.routes, name="routes"),
    path('profile/<str:code>', views.profile, name="profile"),
    path('viewbookings/<int:code>', views.viewbookings, name='viewbookings'),
    path('deleteannouncement/<int:code>', views.deleteannouncement, name="deleteannouncement"),
    path('deletefeedback/<int:code>', views.deletefeedback, name="deletefeedback"),
    path('deletebus/<int:code>', views.deletebus, name="deletebus"),
    path('bookbus/<int:code>/<int:user>', views.bookbus, name="bookbus"),
    path('cancelbus/<int:code>/<int:user>', views.cancelbus, name="cancelbus"),
    
    # API Routes
    path('route/<int:code>', views.route, name="route"),
    path('routestops/<int:code>', views.routestops, name="routestops"),
    path('getlocation/<int:code>', views.getlocation, name="getlocation"),
    path('setlocation/<int:code>', views.setlocation, name="setlocation"),

]