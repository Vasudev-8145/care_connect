from django.shortcuts import render
from django.contrib.auth.models import User

from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from staff.models import Doctor
from staff_v2.serializers import DoctorSerializer,UserSerializer

# Create your views here.

class DoctorListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,request):

        qs = Doctor.objects.all()

        serializer_instance = DoctorSerializer(qs,many = True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = DoctorSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Doctor.objects.create(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

class DoctorRetrieveUpdateDeleteView(APIView):

    def get(post,request,pk=None):

        qs = Doctor.objects.get(id=pk)   # filter annenkil many kodknm qs kynjt

        serializer_instance = DoctorSerializer(qs)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        form_data = request.data

        serializer_instance = DoctorSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Doctor.objects.filter(id=pk).update(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        Doctor.objects.get(id=pk).delete()

        return Response(data={"message":"deleted..."})

class UserCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            # User.objects.create(**form_data) X password not encrypted
            # User.objects.create_user(** form_data) X not an adminuser

            User.objects.create_superuser(**form_data) #superuser

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)