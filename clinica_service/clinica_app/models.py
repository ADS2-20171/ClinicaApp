from django.db import models

# Create your models here.

    # TIPODOC = (('DNI','DNI'),('RUC',RUC))


class Cliente(models.Model):
    DNI = 'DNI'
    RUC = 'RUC'
    TIPODOC = ((DNI, 'DNI'), (RUC, 'RUC'),)
    HOMBRE = 'Hombre'
    MUJER = 'Mujer'
    GENERO = ((HOMBRE, 'Hombre'), (MUJER, 'Mujer'),)
    # ESTADO = ((0, 'Denegado'), (1, 'Activo'),)
    #nombre_cliente = models.CharField(max_length=50, blank=True, null=True, verbose_name='Titulo')
    nombre_cliente = models.CharField(max_length=50, blank=True, null=True)
    apellidos_cliente = models.CharField(max_length=50, blank=True, null=True)
    direccion_cliente = models.CharField(max_length=50, blank=True, null=True)
    telefono_cliente = models.CharField(max_length=9, blank=True, null=True)
    tipodoc_cliente = models.CharField(
        max_length=10, choices=TIPODOC, default=DNI)
    numdoc_cliente = models.IntegerField(blank=True, null=True)
    email_cliente = models.EmailField(max_length=50, null=True)
    genero_cliente = models.CharField(
        max_length=10, choices=GENERO, default=HOMBRE)
    fechasuscripcion_cliente = models.DateField(
        auto_now_add=True, blank=True, null=True)

    # estado_cliente = models.BooleanField(default=True)
    # estado_cliente = models.IntegerField(default=1, choices=ESTADO)
    # foto = models.ImageField(upload_to='foto')

    class Meta:
        ordering = ['nombre_cliente']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __unicode__(self):  # Python 2 para no mostrar "nombre object"
        return self.nombre_cliente

    def __str__(self):  # Python 3 para no mostrar "nombre object"
        return self.nombre_cliente


#class ClienteSerializer(serializers.ModelSerializer):

    #class Meta:
        #model = Cliente
        #ordering = ['nombre_cliente', 'apellidos_cliente']
        #fields = ('id', 'nombre_cliente', 'apellidos_cliente', 'direccion_cliente', 'telefono_cliente',
                  #'tipodoc_cliente', 'numdoc_cliente', 'email_cliente', 'genero_cliente', 'fechasuscripcion_cliente')


#class ClienteViewSet(viewsets.ModelViewSet):  # API REST
    #queryset = Cliente.objects.filter()
    #serializer_class = ClienteSerializer
    #pagination_class = SetPagination
    # paginate_by = 3
    # permission_classes = [permissions.IsAuthenticated]

    #def get_queryset(self):
        #query = self.request.query_params.get('query', '')
        #queryall = (Q(nombre_cliente__icontains=query),
                    #Q(apellidos_cliente__icontains=query),
                    #Q(direccion_cliente__icontains=query),
                    #Q(telefono_cliente__icontains=query),
                    #Q(tipodoc_cliente__icontains=query),
                    #Q(numdoc_cliente__icontains=query),
                    #Q(email_cliente__icontains=query),
                    #Q(genero_cliente=query)),
                    #Q(fechasuscripcion_cliente=query))
        #queryset=self.queryset.filter(reduce(OR, queryall))
        #return queryset
