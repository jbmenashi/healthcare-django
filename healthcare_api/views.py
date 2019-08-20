from django.shortcuts import render
from rest_framework import viewsets
from .models import Symptom, Result
from .serializers import SymptomSerializer, ResultSerializer

class SymptomView(viewsets.ModelViewSet):
   queryset = Symptom.objects.all()
   serializer_class = SymptomSerializer

class ResultView(viewsets.ModelViewSet):
   queryset = Result.objects.all()
   serializer_class = ResultSerializer