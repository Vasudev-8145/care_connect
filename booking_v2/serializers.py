
from rest_framework import serializers
from django.contrib.auth.models import User
from bookings.models import Appointment

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

class AppointmetnSerializerv2(serializers.ModelSerializer):

    class Meta:

        model = Appointment

        fields = "__all__"

    
