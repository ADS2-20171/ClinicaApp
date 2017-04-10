from rest_framework import serializers, viewsets, routers
#from django.contrib.auth.models import User, Group
from django.conf.urls import url, include
from .models import Cliente

# Serializers define the API representation.


class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cliente
        fields = ('url','id', 'nombre_cliente', 'apellidos_cliente', 'direccion_cliente', 'telefono_cliente',
                  'tipodoc_cliente', 'numdoc_cliente', 'email_cliente', 'genero_cliente', 'fechasuscripcion_cliente')


#class UserSerializer(serializers.HyperlinkedModelSerializer):

    #class Meta:
        #model = User
        #fields = ('id', 'username', 'email', 'password','groups')


#class GroupSerializer(serializers.HyperlinkedModelSerializer):

    #class Meta:
        #model = Group
        #fields = ('id', 'name')
