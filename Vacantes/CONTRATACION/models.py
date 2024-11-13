from django.db import models


class Empleado(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.TextField()
    edad = models.IntegerField()
    direccion = models. TextField()
    telefono = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Puesto(models.Model):
    nombre = models.CharField(max_length=100)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    departamento = models.ForeignKey(Departamento, related_name='puestos', on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre


class Contrato(models.Model):
    empleado = models.ForeignKey(Empleado, related_name='contratos', on_delete=models.RESTRICT)
    puesto = models.ForeignKey(Puesto, on_delete=models.RESTRICT)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True) 
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.empleado.nombre
