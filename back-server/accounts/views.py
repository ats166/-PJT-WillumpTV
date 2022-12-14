from django.shortcuts import render
    

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserDetailsSerializer

User = get_user_model()


# Create your views here.
@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserDetailsSerializer(user)
    return Response(serializer.data)