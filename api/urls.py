from django.conf.urls import url, include
from rest_framework import routers
from api import views
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'records', views.RecordViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth', obtain_jwt_token),
    url(r'^signup', views.Singup.as_view(), name='signup'),
    
]
