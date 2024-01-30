from rest_framework import viewsets
from customer.serializers import UserSerializer, ProfileSerializer, LoginSerializer
from customer.models import User, Profile
from rest_framework import permissions
from django.contrib.auth import login

from knox.views import LoginView as KnoxLoginView

from datetime import datetime


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.kwargs['user_pk'])

    def create(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=self.request.data,
                                     context={'request': self.request})
        if serializer.is_valid():
            reg_year = serializer.object.business_reg_date.strftime("%Y")
            now = datetime.now().strftime("%Y")
            serializer.object.business_age = now - reg_year
            serializer.save()
        
    

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
