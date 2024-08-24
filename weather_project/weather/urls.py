from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherViewSet

router = DefaultRouter()
router.register(r'weather', WeatherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from .views import WeatherViewSet, index

router = DefaultRouter()
router.register(r'weather', WeatherViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
