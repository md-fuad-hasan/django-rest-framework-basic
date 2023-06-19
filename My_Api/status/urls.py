from django.urls import path
from .views import StatusViewSet 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'status', StatusViewSet, basename = 'status')

urlpatterns = [] + router.urls