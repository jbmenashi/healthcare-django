from django.db import models



class Result(models.Model):
   title = models.CharField(max_length=100)
   frequency = models.IntegerField()

   def __str__(self):
      return self.title


class Symptom(models.Model):
   title = models.CharField(max_length=100)
   results = models.ManyToManyField(Result)

   def __str__(self):
      return self.title
