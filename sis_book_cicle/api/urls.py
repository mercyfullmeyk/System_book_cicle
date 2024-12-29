from django.urls import include, path
from rest_framework import routers
from api.views import BookViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
