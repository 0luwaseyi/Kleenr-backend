from django.shortcuts import render
from rest_framework import viewsets
from kleenr_app.serializers import signupSerializer, loginSerializer
from kleenr_app.models import signup, login

# Create your views here.

class signupView(viewsets.ModelViewSet):
    serializer_class = signupSerializer
    queryset = signup.objects.all()

class loginView(viewsets.ModelViewSet):
    serializer_class = loginSerializer
    queryset = login.objects.all()