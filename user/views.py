from django.shortcuts import render
from rest_framework import generics
from user.models import Users
from .serializers import UserSerializer

class UserCRUD(generics.GenericAPIView):
    lookup_field = 'pk'
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return Users.objects.all()

