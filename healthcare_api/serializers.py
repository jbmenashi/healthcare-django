from rest_framework import serializers
from .models import Symptom, Result

class ResultSerializer(serializers.ModelSerializer):
   class Meta:
      model = Result
      fields = ('id', 'title', 'frequency')

class SymptomSerializer(serializers.ModelSerializer):
   results = ResultSerializer(many=True)

   class Meta:
      model = Symptom
      fields = ('id', 'title', 'results')


