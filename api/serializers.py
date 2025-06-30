from rest_framework import serializers

from inv.models import Producto
from fac.models import Cliente
from cmp.models import Proveedor

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Producto
        fields='__all__'


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cliente
        fields='__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proveedor
        fields='__all__'
