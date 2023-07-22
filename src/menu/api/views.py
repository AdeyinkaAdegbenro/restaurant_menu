from api.serializers import UserSerializer
from django.contrib.auth.models import User
from .models import Menu, MenuItem
from .rate_limit import CustomRateThrottling
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import MenuSerializer, MenuItemSerializer, MenuItemPostSerializer


# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    throttle_classes = [CustomRateThrottling]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class MenuViewSet(viewsets.ModelViewSet):
    throttle_classes = [CustomRateThrottling]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    throttle_classes = [CustomRateThrottling]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemPostSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = MenuItemSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)
    
    # def retrieve(self, request):
    #     instance = self.get_object()
    #     serializer = MenuItemSerializer(instance=instance)
    #     return Response(serializer.data)