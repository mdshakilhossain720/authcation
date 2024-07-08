from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serilizers import UserProfileSerilizers, UserRegestionSerilizer,UserPasswordSerilizers,UserPasswordResetSerilizers,UserLoginSerilizers,SendPasswordRestSerilizers
from django.contrib.auth import authenticate
from account.renders import UserRenders
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.

class UserRegestionsApiView(APIView):
    renderer_classes=[UserRenders]
    def post(self,request,format=None):
        serilizers=UserRegestionSerilizer(data=request.data)
        if serilizers.is_valid(raise_exception=True):
            user=serilizers.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'Regestion success'},status=status.HTTP_201_CREATED)

        
        return Response(serilizers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginApiView(APIView):
    renderer_classes=[UserRenders]
    def post(self,request,format=None):
        serilizer=UserLoginSerilizers(data=request.data)
        if serilizer.is_valid(raise_exception=True):
            email=serilizer.data.get('email')
            password=serilizer.data.get('password')
            user=authenticate(email = email,password=password)
           # user=serilizer.save()

            if user is not None:
             return Response({'msg':'Login success'},status=status.HTTP_200_OK)
          
            else:
        
             return Response({'errors':{'non_field_errors':['Email or Password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserProfileApi(APIView):
   renderer_classes=[UserRenders]
   permission_classes =[IsAuthenticated]
   def get(self,request,format=None):
      serilizer=UserProfileSerilizers(request.user)

      if serilizer.is_valid():
         return Response(serilizer.data,status=status.HTTP_200_OK)
      


class UserChangePassword(APIView):
   renderer_classes=[UserRenders]
   permission_classes=[IsAuthenticated]
   def post(self,request,format=None):
      serilizer=UserPasswordSerilizers(data=request.data,context={'user':request.user})

      if serilizer.is_valid(raise_exception=True):
         return Response({'msg':'password change succefull'},status=status.HTTP_200_OK)
      return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
   

class SendPasswordResetPasswordEmail(APIView):
   renderer_classes=[UserRenders]
   def post(self,request,format=None):
      serilizer= SendPasswordRestSerilizers(data=request.data)
      if serilizer.is_valid(raise_exception=True):
          return Response({'msg':'password change succefull'},status=status.HTTP_200_OK)
      return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
   




class UserPasswordResetView(APIView):
   renderer_classes=[UserRenders]
   def post(self,request,uid,token,format=None):
      serilizer=UserPasswordResetSerilizers(data=request.data,contex={'uid':uid,'token':token})
      if serilizer.is_valid(raise_exception=True):
         return Response({'msg':'password Rest Succeffull'},status=status.HTTP_200_OK)
      return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
         


    




    
