from django.contrib import admin
from gestion.models import *
# Register your models here.

class ventas_Admin(admin.ModelAdmin):
    list_display=("fecha","cliente_name","email","producto","entregado")
    date_hierarchy = "fecha"
    list_filter = ("fecha","region","pago", "producto", "entregado")
    # Clase con nombres de las columnas q se mostraran en el panel
    # Separar por detalle fieldsets
    fieldsets = (
        (None, {
            'fields': ('fecha', 'cliente_name','cliente_id', 'region', 'producto','cantidad','precio','pago')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('email', 'telefono','direccion', 'comuna','entregado','detalle'),
        }),
    )
    # list_display_links = ('fecha',)

    search_fields=("cliente_name","email") #String: un string-columna por donde buscara
    list_per_page=200

class compra_Admin(admin.ModelAdmin):
    date_hierarchy = "fecha"
    list_display = ('fecha', 'producto', "precio", 'cantidad', 'tc')
    list_filter = ('fecha', 'producto')

class product_Admin(admin.ModelAdmin):
    list_display = ('nombre', 'proveedor', 'equipo')
    list_filter = ['proveedor', 'equipo']
    search_fields = ['nombre', 'equipo']

class proveedor_Admin(admin.ModelAdmin):
    list_display = ('nombre', 'web')

class categoria_Admin(admin.ModelAdmin):
    list_display = ['categoria']

class region_Admin(admin.ModelAdmin):
    list_display = ['region']

class pago_Admin(admin.ModelAdmin):
    list_display = ['metodo']

class equipo_Admin(admin.ModelAdmin):
    list_display = ['equipo']

admin.site.register(Venta, ventas_Admin)  #clientesAdmin clase con nombres a mostrar
admin.site.register(Compra, compra_Admin) 
admin.site.register(Producto, product_Admin)
admin.site.register(Proveedor, proveedor_Admin)
admin.site.register(Categorias, categoria_Admin)
admin.site.register(Region, region_Admin)
admin.site.register(Pago, pago_Admin)
admin.site.register(Equipo, equipo_Admin)