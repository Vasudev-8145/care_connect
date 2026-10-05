from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from booking_v2.serializers import SignUpSerializer

# Create your views here.

class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = SignUpSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            user_object = User.objects.create_user(**cleaned_data)

            serializer_instance = SignUpSerializer(user_object)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

