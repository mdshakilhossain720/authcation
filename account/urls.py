from django.urls import path,include
from account.views import UserRegestionsApiView,UserLoginApiView,UserProfileApi,UserChangePassword,SendPasswordResetPasswordEmail,UserPasswordResetView


urlpatterns = [
    path('regestion/',UserRegestionsApiView.as_view(),name='register'),
    path('userlogin/',UserLoginApiView.as_view(),name='userlogin'),
    path('userprofile/',UserProfileApi.as_view(),name='userprofile'),
    path('changepassword/',UserChangePassword.as_view(),name='changepassword'),
    path('sendrestpasswordemail/',SendPasswordResetPasswordEmail.as_view(),name='sendrestpassword'),
    path('passwordrest/<uid>/<token>/',UserPasswordResetView.as_view(),name='passwordrest'),
]

