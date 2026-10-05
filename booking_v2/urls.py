
from django.urls import path
from booking_v2.views import SignUpView

urlpatterns = [

    path("signup/",SignUpView.as_view()),
]