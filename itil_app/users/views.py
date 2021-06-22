from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import GetUserSerializer, CreateUserSerializer


class CreateUser(generics.GenericAPIView):
	serializer_class = CreateUserSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		token = AuthToken.objects.create(user)
		print(token[0])
		print(token[1])
		return Response({
			'user': GetUserSerializer(user, context=self.get_serializer_context()).data,
		})