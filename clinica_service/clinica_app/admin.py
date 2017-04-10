from django.contrib import admin

# Register your models here.
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_per_page = 5
   #list_display = ("apellidos_paciente", "nombre_paciente")
    list_display = ["nombre_cliente", "apellidos_cliente", "direccion_cliente", "telefono_cliente",
                    "tipodoc_cliente", "numdoc_cliente", "email_cliente", "genero_cliente", "fechasuscripcion_cliente"]
    list_display_links = ["nombre_cliente"]
    list_editable = ["direccion_cliente", "telefono_cliente", "email_cliente"]
    search_fields = ["nombre_cliente", "apellidos_cliente"]

    # class Meta:
    #    model = Cliente

admin.site.register(Cliente, ClienteAdmin)
