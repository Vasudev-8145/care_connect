
from django.urls import path
from booking_v2.views import SignUpView,Appointmentv2ListCreateView

urlpatterns = [

    # authentication routes
    path("signup/",SignUpView.as_view()),

    # appointment v2 list,create route
    path("appointmentv2/",Appointmentv2ListCreateView.as_view()),
]