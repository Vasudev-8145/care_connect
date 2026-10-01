from rest_framework import serializers
from datetime import datetime

class AppoinmentSerializer(serializers.Serializer):

    patient_name = serializers.CharField()

    phone = serializers.CharField()

    doctor = serializers.IntegerField()

    appointment_date = serializers.DateField()

    def validate(self,validated_data):
    
        appointment_date = validated_data.get("appointment_date")

        if appointment_date < datetime.today().date():

            raise serializers.ValidationError("Invalid date")

        return validated_data

    token_number = serializers.IntegerField(read_only=True)

    appointment_time = serializers.TimeField(read_only=True)

    problem = serializers.CharField()

    created_at = serializers.DateTimeField(read_only=True)