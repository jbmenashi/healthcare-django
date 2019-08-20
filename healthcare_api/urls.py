from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('symptoms', views.SymptomView)
router.register('results', views.ResultView)

urlpatterns = [
   path('', include(router.urls))
]
