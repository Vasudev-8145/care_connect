
from rest_framework import serializers
from django.contrib.auth.models import User
from bookings.models import Appointment
from datetime import datetime

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

class AppointmetnSerializerv2(serializers.ModelSerializer):

    doctor = serializers.StringRelatedField()

    class Meta:

        model = Appointment

        fields = "__all__"

        read_only_fields = ["id","token_number","appointment_time","created_at"]

    def validate(self,validated_data):

        appointment_date = validated_data.get("appointment_date")
        doctor = validated_data.get("doctor")
        phone = validated_data.get("phone")

        last_appointment_object = Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date).last()
        details = Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date,phone=phone)

        if details:

            raise serializers.ValidationError("you have already booked a token")
        
        if appointment_date<datetime.today().date():

            raise serializers.ValidationError("Invalid date")

        if last_appointment_object:

            if last_appointment_object.token_number == 25:

                raise serializers.ValidationError("slots full")

        return validated_data

    
