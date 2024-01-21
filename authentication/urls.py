from django.urls import path

from authentication.views import RegisterView, ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("forgot-password/", ForgotPasswordView.as_view(), name='forgot-password'),
    path("reset-password/<str:access>/", ResetPasswordView.as_view(), name='reset-password'),
]
