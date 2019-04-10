from django.conf.urls import url, include
from rest_framework import routers
from api import views
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'records', views.RecordViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth', ObtainAuthToken.as_view()),
    url(r'^signup', views.Singup.as_view(), name='signup')
]
