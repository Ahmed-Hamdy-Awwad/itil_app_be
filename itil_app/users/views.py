from knox.models import AuthToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .serializers import GetUserSerializer, CreateUserSerializer, LoginSerializer


class CreateUser(generics.GenericAPIView):
	serializer_class = CreateUserSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		token = AuthToken.objects.create(user)
		return Response({
			'user': GetUserSerializer(user, context=self.get_serializer_context()).data,
			'toke': token[1]
		})


class Login(generics.GenericAPIView):
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data
		_, token = AuthToken.objects.create(user)
		tokenTTL = AuthToken.objects.filter(user=user).order_by('-created')[0].expiry
		return Response({
				'user': GetUserSerializer(user, context=self.get_serializer_context()).data,
				'token': token,
				'expiry': tokenTTL
			})


class UserView(viewsets.ModelViewSet):
	filter_fields = ('username',)
	# permission_classes = [permissions.DjangoModelPermissions]

	def get_queryset(self):
		return User.objects.all()

	def get_serializer_class(self):
		return GetUserSerializer