from rest_framework import serializers
from kleenr_app.models import signup, login

class signupSerializer(serializers.ModelSerializer):
    class Meta:
        model = signup
        fields = ('firstname', 'lastname', 'email', 'password')

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model  = login
        fields = ('email', 'password')