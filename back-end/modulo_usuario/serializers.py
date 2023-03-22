# import serializers from the REST framework
from rest_framework import serializers
from modulo_usuario.models import usuario
from django.contrib.auth.models import User

# create a serializer class
class user_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = User
		fields = '__all__'

	def create(self,validated_data):
		user = User(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user

class usuario_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = usuario
		fields = '__all__'
 
class User_manage(serializers.Serializer):
	id = serializers.IntegerField()

class Usuario_manage(serializers.Serializer):
    id = serializers.IntegerField()
