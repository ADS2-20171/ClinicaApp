from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializers import ClienteSerializer
#, UserSerializer, GroupSerializer
from rest_framework import viewsets

# Create your views here.
from .forms import ClienteForm
from .models import Cliente
from rest_framework.permissions import IsAuthenticated, IsAdminUser

def inicio(request):
    form = ClienteForm(request.POST or None)  # campos obligatorios
    # print (dir(form)) para saber comandos en cmd
    if form.is_valid():
        form_data = form.cleaned_data
        aba = form_data.get("nombre_cliente")
        abb = form_data.get("apellidos_cliente")
        abc = form_data.get("direccion_cliente")
        abd = form_data.get("telefono_cliente")
        abe = form_data.get("tipodoc_cliente")
        abf = form_data.get("numdoc_cliente")
        abg = form_data.get("email_cliente")
        abh = form_data.get("genero_cliente")
        abi = form_data.get("fechasuscripcion_cliente")
        obj = Cliente.objects.create(nombre_cliente=aba, apellidos_cliente=abb, direccion_cliente=abc, telefono_cliente=abd,
                                     tipodoc_cliente=abe, numdoc_cliente=abf, email_cliente=abg, genero_cliente=abh, fechasuscripcion_cliente=abi)
    context = {
        "var_form": form,
    }
    return render(request, "inicio.html", context)

# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):  # API REST
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsOwnerOrReadOnly,)
    #pagination_class = SetPagination
#con agregar esa sola linea y decir la cantidad de items que tendrá tu página, hace la magia para paginar
    #paginate_by = 3

    def pre_save(self, obj):
        obj.owner = self.request.user
    # def get_queryset(self):
        #query = self.request.query_params.get('query', '')
        # queryall = (Q(nombre_cliente__icontains=query),
        # Q(apellidos_cliente__icontains=query),
        # Q(direccion_cliente__icontains=query),
        # Q(telefono_cliente__icontains=query),
        # Q(tipodoc_cliente__icontains=query),
        # Q(numdoc_cliente__icontains=query),
        # Q(email_cliente__icontains=query),
        # Q(genero_cliente=query)),
        # Q(fechasuscripcion_cliente=query))
        #queryset=self.queryset.filter(reduce(OR, queryall))
        # return queryset

#class UserViewSet(viewsets.ModelViewSet):
    #"""
    #API endpoint that allows users to be viewed or edited.
    #"""
    #queryset = User.objects.all().order_by('-date_joined')
    #serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
#De esta forma sólo damos acceso a este recurso a usuarios de tipo admin
    #permission_classes = (IsAdminUser,)
    #permission_classes = (IsAuthenticated,)

#class GroupViewSet(viewsets.ModelViewSet):
    #"""
    #API endpoint that allows groups to be viewed or edited.
    #"""
    #queryset = Group.objects.all()
    #serializer_class = GroupSerializer
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
