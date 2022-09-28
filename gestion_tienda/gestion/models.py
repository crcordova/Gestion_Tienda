from tabnanny import verbose
from django.db import models

class Pago(models.Model):
    metodo = models.CharField(max_length=20)
    def __str__(self):
        return self.metodo

class Region (models.Model):
    region = models.CharField(max_length=50, verbose_name='Región', primary_key=True)
    def __str__(self):
        return self.region

class Comuna (models.Model):
    comuna = models.CharField(max_length=50, verbose_name='Comuna')
    def __str__(self):
        return self.comuna

    class Meta:
        ordering = ['comuna']

class Proveedor (models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    web = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.nombre

class Categorias (models.Model):
    categoria = models.CharField(max_length=50, verbose_name='Sección')
    def __str__(self):
        return self.categoria

class Equipo (models.Model):
    equipo = models.CharField(max_length=50, verbose_name='Tipo de Equipo') 
    def __str__(self):
        return self.equipo

class Producto(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ManyToManyField(Categorias)
    detalle = models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateField()
    cliente_name = models.CharField(max_length=100, verbose_name='Cliente', blank=True, null=True)
    cliente_id = models.CharField(max_length=12, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=20, decimal_places=0)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    entregado = models.BooleanField()
    detalle = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['fecha']

    def __str__ (self):
        res = str(self.cantidad * self.precio)
        return 'Venta a: %s total %s' %(self.cliente_name, res)
    
class Compra (models.Model):
    fecha = models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=20, decimal_places=3)
    cantidad = models.IntegerField()
    tc = models.DecimalField(verbose_name='Tipo de Cambio', max_digits=20, decimal_places=1)
    detalle = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "Compra de %s %s a la fecha %s" %(self.cantidad, self.producto, self.fecha)
