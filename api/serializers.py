from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Record
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        extra_kwargs = { 'password' : { 'write_only': True, 'required':True } }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('__all__')
    id = serializers.IntegerField(read_only=True)
    distance = serializers.IntegerField()
    time = serializers.IntegerField()
    date = serializers.DateTimeField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
