from django.contrib.auth.models import User
from api.models import Record
from rest_framework import viewsets, views
from .serializers import UserSerializer, RecordSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class Singup(views.APIView):
    def post (self, request, format='json'):
        user_serializer = UserSerializer(data=request.data)
        print (request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            print (user_serializer.data)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)