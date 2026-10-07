
from django.urls import path
from booking_v2.views import SignUpView,Appointmentv2ListCreateView,Appointmentv2RetreiveUpdateDeleteView

urlpatterns = [

    # authentication routes
    path("signup/",SignUpView.as_view()),

    # appointment v2 list,create route
    path("appointmentv2/",Appointmentv2ListCreateView.as_view()),

    # appointment v2 retreive,update,delete route
    path("appointmentv2/<int:pk>/",Appointmentv2RetreiveUpdateDeleteView.as_view()),
]