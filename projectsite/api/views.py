from django.shortcuts import render
from rest_framework import generics
from studentorg.models import College
from .serializers import CollegeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CollegeListCreateAPIView(generics.ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]

class CollegeRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]  