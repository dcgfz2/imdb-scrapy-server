from django.urls import include, path
from rest_framework import routers
from rest_api.views import MovieViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = router.urls
