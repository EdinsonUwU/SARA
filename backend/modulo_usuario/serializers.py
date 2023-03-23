# import serializers from the REST framework
from modulo_usuario.models import user_extended
from rest_framework import serializers
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

class user_extended_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = user_extended
		fields = '__all__'