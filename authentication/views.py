from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from .permissions import IsNotAuthenticated
from .serializers import RegisterSerializer, ResetPasswordSerializer, ForgotPasswordSerializer
from rest_framework import generics, status


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ForgotPasswordView(generics.CreateAPIView):
    queryset = User.objects.all()
    # password can be forgotten only by unauthenticated user
    permission_classes = (IsNotAuthenticated,)
    serializer_class = ForgotPasswordSerializer

    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):
            serializer.send_email()


class ResetPasswordView(generics.UpdateAPIView):
    lookup_url_kwarg = "access"
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer
    permission_classes = (AllowAny,)

    def update(self, request, access, *args, **kwargs):
        token = AccessToken(access)
        user_id = token.payload['user_id']
        if self.queryset.filter(id=user_id).exists():
            partial = kwargs.pop('partial', False)
            user = self.queryset.get(id=user_id)
            serializer = self.serializer_class(user, request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer, user)
            return Response(status=status.HTTP_200_OK)

    def perform_update(self, serializer, user):
        serializer.save(user)









