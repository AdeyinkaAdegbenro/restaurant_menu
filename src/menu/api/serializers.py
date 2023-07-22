from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, MenuItem

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    menu_name = serializers.ReadOnlyField(source='menu.name')
    class Meta:
        model = MenuItem
        fields = ['url', 'name', 'menu_name']

class MenuItemPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    menu_items = MenuItemSerializer(read_only=True, many=True, source='menuitem_set')
    class Meta:
        model = Menu
        fields = ['url', 'name', 'menu_items', 'id']